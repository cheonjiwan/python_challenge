import requests
from flask import Flask, render_template, request
from source import myfunc
import operator
"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/read")
def find():
  read_list=[]
  name_list =[]
  word = request.args
  for a in subreddits:
    if a in word:
      name_list.append(a)
  read_list= myfunc(word)
  sort_list = sorted(read_list, key =(lambda x: x['vote']),reverse=True)
  return render_template("read.html", sort_list = sort_list,name_list = name_list)

app.run(host="0.0.0.0")