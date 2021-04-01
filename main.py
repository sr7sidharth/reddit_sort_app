import os
from dotenv import load_dotenv
import praw
from flask import Flask, request

app = Flask(__name__)

load_dotenv()
secret = os.getenv("secret")
client = os.getenv("client")
redirect = os.getenv("redirect") 
user_agent = os.getenv("user")

reddit = praw.Reddit(
	client_id=client,
	client_secret=secret,
	redirect_uri=redirect,
	user_agent=user_agent
)

@app.route('/')
def main():
	url = reddit.auth.url(["*"], "...", "permanent")
	text = '<a href="%s")>Click here to authorize reddit</a>'
	return text % url

@app.route('/sorted')
def sorted():
	code = request.args.get('code')
	reddit.auth.authorize(code)
	text = ""
	for item in reddit.user.me().saved(limit=50):
		if isinstance(item,praw.models.Submission):
			subreddit = item.subreddit
			if subreddit.display_name == "thefalconandthews":
				text += '<a href="' + str(item.url) + '">'+ str(item.title) + '</a>'
				text += "<br>"
	return text