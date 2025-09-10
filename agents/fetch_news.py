# agents/fetch_news.py
def fetch_news():
    # Examples of security feeds:
    urls = [
        "https://feeds.feedburner.com/TheHackersNews",       # The Hacker News
        "https://www.securityweek.com/feed",                 # SecurityWeek
        "https://www.darkreading.com/rss.xml"                # Dark Reading
    ]
    feed_items = []

    import feedparser
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # limit per feed
            text = f"{entry['title']}\n{entry['summary']}"
            feed_items.append(text)
    return feed_items[:10]  # total max
