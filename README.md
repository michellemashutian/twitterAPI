# Twitter API Integration Script

This repository contains a Python script for interacting with the Twitter API. 
The script allows users to get recent twitter counts based on keyword, recent tweets search based on keyword, analyze tweet content using sentiment analysis, and integrate data from Twitter into their applications.
Links of applied API are listed below:
- Recent twitter counts: https://developer.x.com/en/docs/x-api/tweets/counts/api-reference/get-tweets-counts-recent
- Recent tweets search: https://developer.x.com/en/docs/x-api/tweets/search/quick-start/recent-search
- Sentiment analysis: https://github.com/cjhutto/vaderSentiment

## Features
- Search Tweets: Fetch tweets based on specified keywords and conduct sentiment analysis over english tweets.
- User Timeline: Retrieve the tweets count based on specified keywords.
- Data Output: Outputs retrieved tweets&users/tweet counts in a structured format for further analysis.

## Requirements
To use this script, you need:
- A Twitter Developer Account: Sign up at X Developer(https://developer.x.com/en/portal/dashboard), obtain a **BEARER_TOKEN**.
- Required Python packages (listed in requirements.txt).

## Usage
Before running the script to fetch tweets, you need to: **export BEARER_TOKEN="XXXXX"** in the terminal
or **set BEARER_TOKEN in os environment**.

###
Then you can run script:
```
python main.py
#or you can also run the main function in twitter.py
python twitter.py
```

if you want to
