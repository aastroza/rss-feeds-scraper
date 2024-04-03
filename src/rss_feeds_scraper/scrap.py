from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil import parser
import feedparser
from rss_feeds_scraper.model import Entry, Feed, FeedData

# Code inspired by: https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc

def fetch_rss_data(url: str) -> FeedData:
    feed = feedparser.parse(url)
    f = Feed(
        title = feed.feed.title,
        description = feed.feed.description,
        link = feed.feed.link

    )
    now = datetime.now()
    time_range = timedelta(days=1)

    entries = []

    for entry in feed.entries:
        entry_date = parser.parse(entry.published, ignoretz=True)
        if now - entry_date <= time_range:
            e = Entry(
                title = entry.title,
                link = entry.link,
                published_date = entry_date,
                summary = BeautifulSoup(entry.summary, 'html.parser').get_text()
            )

            entries.append(e)
    
    fd = FeedData(
        feed = f,
        entries = entries
    )

    return fd