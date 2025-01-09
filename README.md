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

### Option 1: Set Parameters Directly in Code
Then you can run script:
```
python main.py
#or you can also run the main function in twitter.py
python twitter.py
```
### Option 2: Use Command-Line Arguments
The script supports command-line arguments via argparse. You can specify parameters in command-Line.
- `--query`: Specify the search query for fetching tweets.
- `--res_number`: Specify the number of tweets to search (range from 10 to 100).
- `--granularity`: Specify the time granularity for tweet count search (which can be day, hour, or minute).

### Twitter API Result
#### Recent twitter counts
```
res: {'data': [{'end': '2025-01-01T00:00:00.000Z', 'start': '2024-12-31T00:13:40.000Z', 'tweet_count': 97875}, {'end': '2025-01-02T00:00:00.000Z', 'start': '2025-01-01T00:00:00.000Z', 'tweet_count': 223020}, {'end': '2025-01-03T00:00:00.000Z', 'start': '2025-01-02T00:00:00.000Z', 'tweet_count': 390596}, {'end': '2025-01-04T00:00:00.000Z', 'start': '2025-01-03T00:00:00.000Z', 'tweet_count': 194315}, {'end': '2025-01-05T00:00:00.000Z', 'start': '2025-01-04T00:00:00.000Z', 'tweet_count': 110810}, {'end': '2025-01-06T00:00:00.000Z', 'start': '2025-01-05T00:00:00.000Z', 'tweet_count': 74770}, {'end': '2025-01-07T00:00:00.000Z', 'start': '2025-01-06T00:00:00.000Z', 'tweet_count': 83240}, {'end': '2025-01-07T00:13:40.000Z', 'start': '2025-01-07T00:00:00.000Z', 'tweet_count': 843}], 'meta': {'total_tweet_count': 1175469}}
```
#### Recent tweets search
```
res: {'data': [{'lang': 'en', 'id': 'XXXXX', 'edit_history_tweet_ids': ['XXXX'], 'public_metrics': {'retweet_count': 5, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 0}, 'text': 'AAAAAAA', 'author_id': 'AA', 'created_at': '2025-01-07T00:13:38.000Z'}, {'lang': 'en', 'id': 'XXXXXX', 'edit_history_tweet_ids': ['XXXXXX'], 'public_metrics': {'retweet_count': 4876, 'reply_count': 0, 'like_count': 0, 'quote_count': 0, 'bookmark_count': 0, 'impression_count': 0}, 'text': 'BBBBBB', 'author_id': 'BB', 'created_at': '2025-01-07T00:13:37.000Z'},.....]}
```
## Limitation
Certain endpoints (like filtered stream and recent search) have a limit on how many Posts they can pull per month.
For Free Plan, limit is 100.

## Contact
For questions or support, feel free to reach out:
- Email: mashutian0608@hotmail.com






