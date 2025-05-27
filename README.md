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

> Note: All visualizations are generated in the notebook:  
> `analysis/news_scraper_analysis.ipynb`

## 📁 Project Structure

news-scraper/

├── data/ # Raw and cleaned data (local cache)

├── db/ # Database-related code

├── analysis/ # Jupyter notebook analysis

├── config/ # Environment variables and DB settings

├── scraping/ # All scraping logic (Selenium, BS4)

├── .env # Not shared (contains DB credentials)

├── requirements.txt # All dependencies

├── README.md

└── .gitignore

## 🛠️ Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/mustafagunuvar/news-scraper-analysis-upwork.git
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Configure PostgreSQL:**
Fill in your .env file with:
```bash
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=news_scraper_db
```
4. **Run the scraper:**
```bash
python scraping/main.py
```
5. **Explore analysis notebook:**
Open analysis/news_scraper_analysis.ipynb in JupyterLab or VSCode.

🔐 Security Note
Sensitive credentials are excluded from version control via .gitignore.
Remember to never commit .env files or database passwords publicly.

📬 Contact
For inquiries or freelance work, feel free to reach out:
📧 mustafa.gunuvar94@gmail.com

⚠️ This project is for educational and professional portfolio purposes. The scraper respects Hacker News request limits and uses polite intervals between requests.





