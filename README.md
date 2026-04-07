# 🛫 Big Data Pipeline — Airline Tweet Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PySpark](https://img.shields.io/badge/PySpark-4.1.1-orange)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Bonus](https://img.shields.io/badge/Bonus-Completed-gold)

---

## 📌 Overview

This project implements a complete **Big Data processing pipeline** using **Apache Spark** and **MongoDB** to ingest, process, analyze, and visualize large-scale Twitter data about US airline sentiment.

The pipeline covers:
- ✅ Data ingestion and cleaning using PySpark
- ✅ NoSQL storage in MongoDB with optimized schema and indexing
- ✅ Large-scale data analysis using Spark transformations
- ✅ Complex querying using Spark SQL
- ✅ Performance comparison between Spark SQL and MongoDB Aggregation
- ✅ Data visualization using Matplotlib and Seaborn
- ✅ **BONUS** — Interactive dashboard using Streamlit
- ✅ **BONUS** — Format comparison: CSV vs Parquet vs Avro

---

## 👥 Team Members

| Member | Responsibility |
|--------|---------------|
| Rabaya Khatun Keya | Data ingestion, cleaning & MongoDB storage |
| Manasha Siriwardana Mudalige Don| Spark processing & transformations |
| Md Firoz Chowdhury | MongoDB queries & indexing |
| Neeru Neeru|| Spark SQL queries & performance analysis | Visualization, report, dashboard & documentation also git process|

---

## 📊 Dataset

| Detail | Info |
|--------|------|
| **Name** | Twitter US Airline Sentiment |
| **Source** | Kaggle |
| **Records** | 14,478 tweets (after cleaning) |
| **Airlines** | United, US Airways, American, Southwest, Delta, Virgin America |
| **Period** | February 2015 |
| **Labels** | Positive, Neutral, Negative |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Apache Spark (PySpark) | 4.1.1 | Large-scale data processing |
| MongoDB | 7.0 | NoSQL data storage |
| Python | 3.x | Programming language |
| Pandas | Latest | Data manipulation |
| Matplotlib | Latest | Static visualizations |
| Seaborn | Latest | Statistical charts |
| Streamlit | Latest | Interactive dashboard |
| Plotly | Latest | Interactive charts in dashboard |
| fastavro | Latest | Avro format support  |
| Google Colab | Linux | Parquet/Avro comparison  |
| Java JDK | 17.0 | Spark runtime |
| Jupyter Notebook | Latest | Development environment |

---

## 📁 Project Structure

```
BIGDATAPROJECT/
│
├── data/
│   └── Tweets.csv                      # Raw dataset
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb         # Load, clean & store in MongoDB
│   ├── 02_spark_processing.ipynb       # PySpark transformations & analysis
│   ├── 03_mongodb_queries.ipynb        # MongoDB aggregation queries
│   ├── 04_spark_sql_queries.ipynb      # Spark SQL & performance comparison
│   ├── 05_visualization.ipynb          # Charts & key insights
│   └── 06_format_comparison.ipynb      # CSV vs Parquet vs Avro 
│
├── report/
│   ├── final_report.pdf                # Final project report
│   ├── chart1_sentiment_pie.png        # Sentiment distribution
│   ├── chart2_airline_sentiment.png    # Sentiment by airline
│   ├── chart3_negative_reasons.png     # Top negative reasons
│   ├── chart4_heatmap.png              # Confidence heatmap
│   └── chart5_performance.png          # Spark vs MongoDB performance
│
├── schema/
│   └── mongo_schema.md                 # MongoDB schema design
│
├── app.py                              # Streamlit dashboard 
├── .gitignore                          # Git ignore file
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Anaconda / Miniconda installed
- Java JDK 17 installed
- MongoDB 7.0 installed and running

### Step 1 — Create Conda Environment
```bash
conda create -n pyspark_env python=3.10
conda activate pyspark_env
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Set Environment Variables
```python
import os
os.environ["JAVA_HOME"]      = r"C:\Users\hp\AppData\Local\Programs\Eclipse Adoptium\jdk-17.0.18.8-hotspot"
os.environ["HADOOP_HOME"]    = r"C:\hadoop"
os.environ["PYSPARK_PYTHON"] = r"C:\Users\hp\anaconda3\envs\pyspark_env\python.exe"
```

### Step 4 — Start MongoDB
```bash
net start MongoDB
```

### Step 5 — Launch Jupyter
```bash
conda activate pyspark_env
jupyter notebook
```

---

## 🚀 How to Run

### Main Notebooks — Run in Order

| Order | Notebook | Description |
|-------|----------|-------------|
| 1st | `01_data_ingestion.ipynb` | Load CSV → clean → store in MongoDB |
| 2nd | `02_spark_processing.ipynb` | Spark transformations & analysis |
| 3rd | `03_mongodb_queries.ipynb` | MongoDB aggregation queries |
| 4th | `04_spark_sql_queries.ipynb` | Spark SQL & performance comparison |
| 5th | `05_visualization.ipynb` | Generate all charts |
| 6th | `06_format_comparison.ipynb` | CSV vs Parquet vs Avro (Google Colab) |

### Streamlit Dashboard (Bonus)
```bash
conda activate pyspark_env
python -m streamlit run app.py
```
Open browser at: `http://localhost:8501`

---

## 🗄️ MongoDB Schema

```
Database:   tweets_db
Collection: airline_tweets

Fields:
  tweet_id                      String
  airline_sentiment             String (positive / neutral / negative)
  airline_sentiment_confidence  Float
  negativereason                String (nullable)
  airline                       String
  retweet_count                 Integer
  text                          String
  clean_text                    String
  tweet_created                 String
  tweet_location                String (nullable)

Indexes (6 total):
  airline                       Single field
  airline_sentiment             Single field
  negativereason                Single field
  tweet_id                      Single field
  airline + airline_sentiment   Compound
```

---

## 📈 Key Findings

### Sentiment Distribution
| Sentiment | Count | Percentage |
|-----------|-------|------------|
| Negative | 9,110 | 63% |
| Neutral | 3,069 | 21% |
| Positive | 2,299 | 16% |

### Airline Rankings
| Rank | Airline | Negative | Positive |
|------|---------|----------|----------|
| 1 (Worst) | United | 2,630 | 492 |
| 2 | US Airways | 2,263 | 269 |
| 3 | American | 1,863 | 307 |
| 4 | Southwest | 1,185 | 570 |
| 5 | Delta | 953 | 544 |
| 6 (Best) | Virgin America | 181 | 152 |

### Top Complaint Reasons
| Rank | Reason | Count |
|------|--------|-------|
| 1 | Customer Service Issue | 2,883 |
| 2 | Late Flight | 1,648 |
| 3 | Can't Tell | 1,175 |
| 4 | Cancelled Flight | 829 |
| 5 | Lost Luggage | 717 |

---

## ⚡ Performance Comparison

### Spark SQL vs MongoDB
| Tool | Best For |
|------|---------|
| MongoDB | Simple aggregations with indexed fields |
| Spark SQL | Complex multi-column analytical queries |

### Format Comparison — Bonus (Google Colab / Linux)
| Format | Write Speed | Read Speed | File Size | Best For |
|--------|------------|------------|-----------|---------|
| CSV | Slowest | Slowest | Largest | Human readable, compatibility |
| Parquet | Medium | Fastest | Smallest | Analytics, fast reads |
| Avro | Fast | Medium | Medium | Streaming, schema evolution |

---

## 🎯 Bonus Features Completed

### ✅ Bonus 1 — Interactive Streamlit Dashboard
- Live connection to MongoDB
- Sidebar filters by airline and sentiment
- Interactive pie chart, bar charts, heatmap
- Airline scorecard table with positive/negative percentages
- Raw data viewer with 100 tweets
- Run with: `python -m streamlit run app.py`

### ✅ Bonus 2 — Format Comparison (CSV vs Parquet vs Avro)
- Tested on Google Colab (Linux environment)
- Used Apache Spark 4.0.2 with fastavro library
- Compared write speed, read speed and file size
- Parquet proved fastest for analytics workloads
- Avro best suited for streaming pipelines
- CSV most compatible and human readable

---

## 📋 Requirements

```
pyspark
pymongo
pandas
matplotlib
seaborn
numpy
streamlit
plotly
fastavro
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📝 Notebooks Summary

### 01 — Data Ingestion
- Loads raw CSV using PySpark
- Cleans text: removes URLs, @mentions, special characters
- Removes duplicates and null values
- Stores 14,478 clean records in MongoDB
- Creates 6 optimized indexes

### 02 — Spark Processing
- Overall sentiment distribution analysis
- Sentiment breakdown by individual airline
- Word frequency analysis on negative tweets (with stopword removal)
- Most retweeted tweets identification
- Average sentiment confidence scores per airline

### 03 — MongoDB Queries
- Aggregation pipeline for sentiment counts
- Airline-level sentiment breakdown
- Top 10 negative complaint reasons
- Index performance testing and timing
- Best and worst airline identification

### 04 — Spark SQL Queries
- Sentiment distribution with percentage using window functions
- Airline scorecard showing positive/neutral/negative breakdown
- Top negative reason per airline
- Hourly tweet activity pattern analysis
- Spark SQL vs MongoDB performance comparison (3-run average)

### 05 — Visualization
- Pie chart: overall sentiment distribution
- Grouped bar chart: sentiment by airline
- Horizontal bar chart: top 10 negative reasons
- Heatmap: average sentiment confidence by airline
- Performance bar chart: Spark SQL vs MongoDB

### 06 — Format Comparison
- Write and read CSV, Parquet, Avro formats
- Compare write speed, read speed and file sizes
- Final summary table with format recommendations
- Run on Google Colab for Linux environment support

---

## 🔮 Future Improvements

- [x] Interactive dashboard using Streamlit ✅
- [x] Compare CSV vs Parquet vs Avro formats ✅
- [ ] Real-time streaming with Spark Streaming
- [ ] ML sentiment classifier using Spark MLlib
- [ ] Deploy on cloud (AWS / GCP) for full Hadoop support
- [ ] Batch vs stream processing comparison

---

## 📄 License

This project is for academic purposes only.

---

## 🙏 Acknowledgements

- Dataset: [Kaggle — Twitter US Airline Sentiment](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
- Apache Spark Documentation: https://spark.apache.org/docs/latest/
- MongoDB Documentation: https://www.mongodb.com/docs/
- Streamlit Documentation: https://docs.streamlit.io/
