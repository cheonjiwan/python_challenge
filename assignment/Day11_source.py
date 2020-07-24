import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
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


def cont_func(word):
  red_list =[]
  for a in subreddits:
    if a in word:
      url = f"https://reddit.com/r/{a}/top/?t=month"
      req = requests.get(url,headers=headers)
      soup = BeautifulSoup(req.text,"html.parser")
      soup_list = soup.find_all('div',{"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
      for temp in soup_list:
        dic = {'title':"",'vote':"",'url':"",'name':a}
        if temp.find('span',{"class":"_2oEYZXchPfHwcf9mTMGMg8"}):
          continue
        if 'k' in temp.find('div',{"class":"_1rZYMD_4xY3gRcSS3p8ODO"}).text:
          continue
        dic['vote'] = int(temp.find('div',{"class":"_1rZYMD_4xY3gRcSS3p8ODO"}).text)
        dic['title'] = temp.find('h3').text
        dic['url']= temp.find('a')["href"]
        red_list.append(dic)
 

  return red_list
    

