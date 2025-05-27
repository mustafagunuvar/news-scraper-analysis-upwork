from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scrape_hacker_news(pages=50):
    """
    Scrapes Hacker News articles from multiple pages.

    Args:
        pages (int): Number of pages to scrape.

    Returns:
        pd.DataFrame: A DataFrame containing titles, links, scores, authors, and comments.
    """
    # Configure headless Chrome browser
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    titles, links, scores, authors, comments = [], [], [], [], []

    base_url = "https://news.ycombinator.com/news?p="

    for page in range(1, pages + 1):
        url = f"{base_url}{page}"
        driver.get(url)
        time.sleep(2)  # Let the page load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        articles = soup.select(".athing")
        subtexts = soup.select(".subtext")

        for article, sub in zip(articles, subtexts):
            # Extract title and link
            title_tag = article.select_one(".titleline a")
            title = title_tag.text.strip()
            link = title_tag["href"]

            # Extract score
            score_tag = sub.select_one(".score")
            score = int(score_tag.text.replace(" points", "")) if score_tag else 0

            # Extract author
            author_tag = sub.select_one(".hnuser")
            author = author_tag.text if author_tag else "N/A"

            # Extract comment count
            comment_tag = sub.select("a")[-1]
            comment_text = comment_tag.text
            comment = comment_text if "comment" in comment_text else "0 comments"

            # Append to lists
            titles.append(title)
            links.append(link)
            scores.append(score)
            authors.append(author)
            comments.append(comment)

    driver.quit()

    # Create DataFrame
    df = pd.DataFrame({
        "title": titles,
        "link": links,
        "score": scores,
        "author": authors,
        "comments": comments
    })

    return df





