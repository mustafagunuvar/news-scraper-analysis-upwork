from scraper.hacker_news_scraper import scrape_hacker_news
from database.db_handler import insert_articles  # You need to have this function ready

def main():
    print("🔍 Scraping Hacker News (50 pages)...")
    articles_df = scrape_hacker_news(pages=50)

    print(f"✅ Scraping completed. Total articles: {len(articles_df)}")
    print(articles_df.head())

    print("💾 Inserting articles into the PostgreSQL database...")
    insert_articles(articles_df)  # Assumes your db_handler.py has a working insert function
    print("✅ Data inserted successfully.")

if __name__ == "__main__":
    main()

