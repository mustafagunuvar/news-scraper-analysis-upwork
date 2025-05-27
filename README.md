# 📰 News Scraper & Analysis with PostgreSQL

This project is a **real-time data scraper and analyzer** built with Python and PostgreSQL. It collects news articles from the popular [Hacker News](https://news.ycombinator.com/) platform and performs advanced analysis on the dataset, including sentiment trends, top authors, headline word frequencies, and engagement metrics.

## 🚀 Key Features

- ✅ **Live Data Scraping**: Dynamically scrapes latest news from Hacker News (updated regularly).
- ✅ **Structured Data Storage**: Clean data is saved in a normalized PostgreSQL database via SQLAlchemy.
- ✅ **Word Cloud & Visual Analysis**: Insightful visualizations with Matplotlib, Seaborn, and WordCloud.
- ✅ **Trend & Engagement Metrics**:
  - Top authors by score & comments
  - Score vs. headline length analysis
  - Most frequent headline keywords
- ✅ **Modular Project Structure**: Easily scalable and ready for deployment.

## 🧱 Tech Stack

| Area | Technology |
|------|------------|
| Backend | `Python`, `Requests`, `BeautifulSoup`, `Selenium` |
| Data Storage | `PostgreSQL` via `SQLAlchemy` and `dbeaver` |
| Analysis | `Pandas`, `NumPy` |
| Visualization | `Matplotlib`, `Seaborn`, `WordCloud` |
| Environment | `venv`, `.env` for secure credentials |

## 🧮 Database Structure

All scraped news articles are stored in a PostgreSQL database using the `psycopg2` driver and SQLAlchemy ORM. The schema includes fields such as:

- `id`
- `title`
- `url`
- `score`
- `num_comments`
- `author`
- `posted_time`

Environment-specific credentials (host, port, user, password, database) are safely stored in a `.env` file and **excluded from GitHub using `.gitignore`**.

## 📊 Sample Visualizations

- WordCloud of Most Common Headline Terms  
- Distribution of Scores by Headline Length  
- Most Active Authors by Total Comments  
- Hourly News Posting Frequency

<p align="center">
  <img src="assets/wordcloud_example.png" width="500" />
</p>

> Note: All visualizations are generated in the notebook:  
> `analysis/news_scraper_analysis.ipynb`

## 📁 Project Structure

