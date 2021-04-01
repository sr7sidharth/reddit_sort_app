import os, sys
from dotenv import load_dotenv
import praw
from mdutils.mdutils import MdUtils

if __name__ == "__main__":
	load_dotenv()
	secret = os.getenv("secret")
	client = os.getenv("client")
	redirect = os.getenv("redirect") 
	user_agent = os.getenv("user_2")
	username = sys.argv[1]
	password = sys.argv[2]

	reddit = praw.Reddit(
	client_id=client,
	client_secret=secret,
	redirect_uri=redirect,
	user_agent=user_agent,
	username=username,
	password=password
	)

	mdFile = MdUtils(file_name="results"+str(sys.argv[3]), title="Found results for: " + str(sys.argv[3]))

	for item in reddit.user.me().saved(limit=int(sys.argv[4]) if len(sys.argv) == 5 else None):
		if isinstance(item,praw.models.Submission):
			subreddit = item.subreddit
			if subreddit.display_name == str(sys.argv[3]):
				mdFile.new_line(str(item.title) + mdFile.new_inline_link(link=str(item.url), text="Link"))
	mdFile.create_md_file()
