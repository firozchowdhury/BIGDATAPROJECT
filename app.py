import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pymongo import MongoClient

# ─── PAGE CONFIG ──────────────────────────────────────────
st.set_page_config(
    page_title="Airline Tweet Sentiment Dashboard",
    page_icon="✈️",
    layout="wide"
)

# ─── LOAD DATA FROM MONGODB ───────────────────────────────
@st.cache_data
def load_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["tweets_db"]
    collection = db["airline_tweets"]
    data = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(data)

    #  THIS IS THE CRITICAL FIX — convert string to float
    df["airline_sentiment_confidence"] = pd.to_numeric(
        df["airline_sentiment_confidence"], errors="coerce"
    )
    df["retweet_count"] = pd.to_numeric(
        df["retweet_count"], errors="coerce"
    ).fillna(0).astype(int)

    return df

# ─── HEADER ───────────────────────────────────────────────
st.title("✈️ Airline Tweet Sentiment Analysis")
st.markdown("**Big Data Pipeline — Apache Spark & MongoDB**")
st.markdown("---")

# Load data
with st.spinner("Loading data from MongoDB..."):
    df = load_data()

# ─── SIDEBAR FILTERS ──────────────────────────────────────
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("---")

# Airline filter
all_airlines = ["All Airlines"] + sorted(df["airline"].unique().tolist())
selected_airline = st.sidebar.selectbox("Select Airline", all_airlines)

# Sentiment filter
all_sentiments = ["All Sentiments", "positive", "neutral", "negative"]
selected_sentiment = st.sidebar.selectbox("Select Sentiment", all_sentiments)

# Apply filters
filtered_df = df.copy()
if selected_airline != "All Airlines":
    filtered_df = filtered_df[filtered_df["airline"] == selected_airline]
if selected_sentiment != "All Sentiments":
    filtered_df = filtered_df[filtered_df["airline_sentiment"] == selected_sentiment]

st.sidebar.markdown("---")
st.sidebar.metric("Total Tweets", f"{len(filtered_df):,}")
st.sidebar.metric("Airlines", filtered_df["airline"].nunique())

# ─── TOP METRICS ──────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

total = len(filtered_df)
positive = len(filtered_df[filtered_df["airline_sentiment"] == "positive"])
neutral = len(filtered_df[filtered_df["airline_sentiment"] == "neutral"])
negative = len(filtered_df[filtered_df["airline_sentiment"] == "negative"])

col1.metric("📊 Total Tweets", f"{total:,}")
col2.metric("😊 Positive", f"{positive:,}",
            f"{positive/total*100:.1f}%" if total > 0 else "0%")
col3.metric("😐 Neutral", f"{neutral:,}",
            f"{neutral/total*100:.1f}%" if total > 0 else "0%")
col4.metric("😠 Negative", f"{negative:,}",
            f"{negative/total*100:.1f}%" if total > 0 else "0%")

st.markdown("---")

# ─── ROW 1: PIE CHART + BAR CHART ─────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Sentiment Distribution")
    sent_counts = filtered_df["airline_sentiment"].value_counts().reset_index()
    sent_counts.columns = ["sentiment", "count"]
    colors = {"positive": "#2ecc71", "neutral": "#f39c12", "negative": "#e74c3c"}
    fig1 = px.pie(
        sent_counts, values="count", names="sentiment",
        color="sentiment", color_discrete_map=colors,
        hole=0.4
    )
    fig1.update_traces(textposition="inside", textinfo="percent+label")
    fig1.update_layout(height=400, showlegend=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("✈️ Sentiment by Airline")
    airline_sent = filtered_df.groupby(
        ["airline", "airline_sentiment"]
    ).size().reset_index(name="count")
    fig2 = px.bar(
        airline_sent, x="airline", y="count",
        color="airline_sentiment",
        color_discrete_map=colors,
        barmode="group"
    )
    fig2.update_layout(height=400, xaxis_tickangle=-30)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ─── ROW 2: NEGATIVE REASONS + HEATMAP ────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("❗ Top Negative Reasons")
    neg_df = filtered_df[
        (filtered_df["airline_sentiment"] == "negative") &
        (filtered_df["negativereason"].notna())
    ]
    if len(neg_df) > 0:
        neg_reasons = neg_df["negativereason"].value_counts().head(10).reset_index()
        neg_reasons.columns = ["reason", "count"]
        fig3 = px.bar(
            neg_reasons, x="count", y="reason",
            orientation="h",
            color="count",
            color_continuous_scale="Reds"
        )
        fig3.update_layout(height=400, yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No negative tweets in current selection")

with col2:
    st.subheader("🔥 Confidence Heatmap by Airline")
    heatmap_data = filtered_df.groupby(
        ["airline", "airline_sentiment"]
    )["airline_sentiment_confidence"].mean().reset_index()
    heatmap_pivot = heatmap_data.pivot(
        index="airline",
        columns="airline_sentiment",
        values="airline_sentiment_confidence"
    ).fillna(0)
    fig4 = px.imshow(
        heatmap_pivot,
        color_continuous_scale="RdYlGn",
        aspect="auto",
        text_auto=".2f"
    )
    fig4.update_layout(height=400)
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# ─── ROW 3: AIRLINE SCORECARD TABLE ───────────────────────
st.subheader("🏆 Airline Scorecard")
scorecard = filtered_df.groupby("airline")["airline_sentiment"].value_counts().unstack(fill_value=0)
for col in ["positive", "neutral", "negative"]:
    if col not in scorecard.columns:
        scorecard[col] = 0
scorecard = scorecard[["positive", "neutral", "negative"]]
scorecard["total"] = scorecard.sum(axis=1)
scorecard["positive %"] = (scorecard["positive"] / scorecard["total"] * 100).round(1)
scorecard["negative %"] = (scorecard["negative"] / scorecard["total"] * 100).round(1)
scorecard = scorecard.sort_values("negative %", ascending=True)
st.dataframe(scorecard, use_container_width=True)

st.markdown("---")

# ─── ROW 4: RAW DATA ──────────────────────────────────────
st.subheader("📋 Raw Tweet Data")
show_cols = ["airline", "airline_sentiment", "negativereason",
             "retweet_count", "text"]
available_cols = [c for c in show_cols if c in filtered_df.columns]
st.dataframe(
    filtered_df[available_cols].head(100),
    use_container_width=True
)

# ─── FOOTER ───────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "**Big Data Project** — Apache Spark 4.1.1 | MongoDB 7.0 | Streamlit"
)

