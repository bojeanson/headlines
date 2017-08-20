import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'lequipe': 'http://www.lequipe.fr/rss/actu_rss_Football.xml',
             'lemonde': 'http://www.lemonde.fr/rss/une.xml'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    title = first_article.get("title")
    title = title.encode('utf-8') if title else ''
    published = first_article.get("published")
    published = published.encode('utf-8') if published else ''
    summary = first_article.get("summary")
    summary = summary.encode('utf-8') if summary else ''
    return render_template("home.html", title=title, published=published, summary=summary)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

