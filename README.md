## Simple application, done in 2 slightly different ways, to sort through saved posts for ones from a specific subreddit.  

## Prerequisites  
- set up your environment with client_id, client_secret and redirect_uri that can be found [here](https://www.reddit.com/prefs/apps). More thorough instructions are found on Reddit's API documentation page on [Github](https://github.com/reddit-archive/reddit/wiki/API) and live API documentation page on [Reddit](https://www.reddit.com/dev/api). 
- install [flask](https://flask.palletsprojects.com/en/1.1.x/), [praw](https://praw.readthedocs.io/en/latest/), and [mdutils](https://mdutils.readthedocs.io/en/latest/) as required. 

## Filename: main.py

- First off, sorry for the nondescript filename haha.
- This follows OAuth2 authentication flow. A quick guide can be found [here](https://github.com/reddit-archive/reddit/wiki/OAuth2).  
- Runs on a Flask server.  

## Filename: script_only.py

- Script version of main.py.  
- Invoke  by  
```
python script_only.py *username* *password* *subdreddit_name* *limit*(optional)
```


Log into reddit account -> Application views saved posts and sorts by subreddit or by nsfw/spoiler tag -> outputs to viewable html file