import feedparser
import validators
import sys
import re

link = str(input())
print('Your link is ' + link)

if(validators.url(link) == False):
    print('URL is not valid')
    sys.exit(0)

rss = feedparser.parse(link)

if(rss.feed.title):
    print('Title:', rss.feed.title)
if(rss.feed.description):
    TAG_RE = re.compile(r'<[^>]+>')
    print(TAG_RE.sub('', rss.feed.description))
if(rss.feed.link):
    print('Url:', rss.feed.link)