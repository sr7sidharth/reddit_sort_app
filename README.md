# Simple application, done in 2 slightly different ways, to sort through saved posts for ones from a specific subreddit.  

## Prerequisites  

- set up your environment with client_id, client_secret and redirect_uri that can be found [here](https://www.reddit.com/prefs/apps). More thorough instructions are found on Reddit's API documentation page on [Github](https://github.com/reddit-archive/reddit/wiki/API) and live API documentation page on [Reddit](https://www.reddit.com/dev/api). 
- install [flask](https://flask.palletsprojects.com/en/1.1.x/), [praw](https://praw.readthedocs.io/en/latest/), and [mdutils](https://mdutils.readthedocs.io/en/latest/) as required. 


## Features

- Goes through a user's saved posts to filter out posts from a specific subreddit

### Filename: main.py

- This follows OAuth2 authentication flow. A quick guide can be found [here](https://github.com/reddit-archive/reddit/wiki/OAuth2).  
- Runs on a Flask server.

### Filename: script_only.py

- Script version of main.py.  
- Invoke with:```python script_only.py *username* *password* *subdreddit_name* *limit*(optional)```
