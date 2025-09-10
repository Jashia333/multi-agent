import feedparser

def fetch_news():
    url= "https://news.google.com/rss"
    feed=feedparser.parse(url)
    return [entry["title"] + "\n" + entry["summary"] for entry in feed.entries[:5]]