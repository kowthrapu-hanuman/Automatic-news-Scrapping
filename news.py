
import newspaper
import feedparser
import lxml.html.clean 

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        try: 
            article = newspaper.Article(entry.link)
            article.download()
            article.parse()

            articles.append({
                'title': article.title,
                'author': article.authors,
                'publish_date': article.publish_date,
                'content': article.text
            })
        except Exception as e: 
            print(f"Error processing article {entry.link}: {e}")
            continue 
    return articles


feed_url = 'http://feeds.bbci.co.uk/news/rss.xml'
articles = scrape_news_from_feed(feed_url)


for article in articles:
    print('Title:', article['title'])
    print('Author:', article['author'])
    print('Publish Date:', article['publish_date'])
    print('Content:', article['content'])
    print()