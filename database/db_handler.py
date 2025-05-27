import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv

# Load env variables (optional but recommended)
load_dotenv()

# PostgreSQL connection configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "news_scraper"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "1234"),
}

def create_connection():
    return psycopg2.connect(**DB_CONFIG)

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS hacker_news (
        id SERIAL PRIMARY KEY,
        title TEXT,
        link TEXT,
        score INTEGER,
        author TEXT,
        comments TEXT,
        scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def insert_articles(articles_df):
    conn = create_connection()
    cur = conn.cursor()

    articles = articles_df.to_dict(orient="records")  # ✅ Buraya dikkat!

    values = [
        (item["title"], item["link"], item["score"], item["author"], item["comments"])
        for item in articles
    ]

    insert_query = """
    INSERT INTO articles (title, link, score, author, comments)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (link) DO NOTHING;
    """

    cur.executemany(insert_query, values)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Articles inserted into the database.")

