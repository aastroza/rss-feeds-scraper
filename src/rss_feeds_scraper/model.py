from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import List

class Entry(BaseModel):
    title: str = None
    link: HttpUrl = None
    published_date: datetime = None
    summary: str = None

class Feed(BaseModel):
    title: str = None
    description: str = None
    link: HttpUrl = None

class FeedData(BaseModel):
    feed: Feed
    entries: List[Entry]

class Data(BaseModel):
    feeds: List[FeedData]