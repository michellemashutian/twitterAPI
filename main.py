import argparse
from twitter import Twitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_args():
    parser = argparse.ArgumentParser(description="A simple argparse example script")

    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="input query"
    )

    parser.add_argument(
        "--granularity",
        type=str,
        required=True,
        help="hour or day"
    )

    parser.add_argument(
        "--res_number",
        type=int,  # Type of the argument
        required=True,
        default=10,
        help="result number"
    )

    args = parser.parse_args()
    return args


def parse_search_count(count_input):
    last_time = []
    data = count_input["data"]
    # total = count_input["meta"]
    for time in data:
        tweet_count = time["tweet_count"]
        start = time["start"]
        end = time["end"]
        last_time.append([start, end, tweet_count])
    last_time.sort()
    return last_time


def text_clean(text_input):
    text_no_newlines = text_input.replace("\n", " ")
    text_no_extra_spaces = " ".join(text_no_newlines.split())
    return text_no_extra_spaces


def eng_txt_sentiment_count(data):
    analyzer = SentimentIntensityAnalyzer()
    pos_count, neg_count, neu_count = 0, 0, 0
    pos_text, neg_text, neu_text = [], [], []
    sentiment_text = []
    for twee in data:
        if twee["lang"] == "en":
            text = text_clean(twee["text"])
            created_at = twee["created_at"]
            '''
            text_id = twee["id"]
            retweet_count = public_metrics["retweet_count"]
            reply_count = public_metrics["reply_count"]
            like_count = public_metrics["like_count"]
            quote_count = public_metrics["quote_count"]
            bookmark_count = public_metrics["bookmark_count"]
            impression_count = public_metrics["impression_count"]
            author_id = twee["author_id"]
            public_metrics = twee["public_metrics"]
            '''
            # sentiment score
            vs = analyzer.polarity_scores(text)
            # pos = vs["pos"]
            # neu = vs["neu"]
            # neg = vs["neg"]
            compound = vs["compound"]
            if compound <= -0.05:
                neg_count += 1
                neg_text.append([created_at, text])
                sentiment_text.append(["neg", created_at, text])
            elif compound >= 0.05:
                pos_count += 1
                pos_text.append([created_at, text])
                sentiment_text.append(["pos", created_at, text])
            else:
                neu_count += 1
                neu_text.append([created_at, text])
                sentiment_text.append(["neu", created_at, text])

    print(f"positive twitter count: {pos_count}")
    print(pos_text, "\n")
    print(f"negative twitter count: {neg_count}")
    print(neg_text, "\n")
    print(f"neutral twitter count: {neu_count}")
    print(neu_text, "\n")
    return sentiment_text


def parse_recent_search(search_input):
    data = search_input["data"]
    users = search_input["includes"]["users"]
    user_dict = {}
    twitter_dict = {}
    for user in users:
        public_metrics = user["public_metrics"]
        followers_count = public_metrics["followers_count"]
        following_count = public_metrics["following_count"]
        tweet_count = public_metrics["tweet_count"]
        listed_count = public_metrics["listed_count"]
        id = user["id"]
        name = user["name"]
        verified = user["verified"]
        user_dict[id] = [name, verified, followers_count, following_count, tweet_count, listed_count]

    for twee in data:
        text_id = twee["id"]
        text = text_clean(twee["text"])
        public_metrics = twee["public_metrics"]
        retweet_count = public_metrics["retweet_count"]
        reply_count = public_metrics["reply_count"]
        like_count = public_metrics["like_count"]
        quote_count = public_metrics["quote_count"]
        bookmark_count = public_metrics["bookmark_count"]
        impression_count = public_metrics["impression_count"]
        created_at = twee["created_at"]
        author_id = twee["author_id"]
        twitter_dict[text_id]: [text, author_id, created_at, retweet_count, reply_count, like_count, quote_count,
                                bookmark_count, impression_count]

    sentiment_text_list = eng_txt_sentiment_count(data)
    return user_dict, twitter_dict, sentiment_text_list


if __name__ == "__main__":
    twitter = Twitter()
    query = "tesla"
    granularity = "day"  # should be set when search count, hour or day
    res_search_count = twitter.search_count(query, granularity)
    time_counts = parse_search_count(res_search_count)
    print(f"twitter count in last 8 time slots: {time_counts}\n")
    res_search_recent = twitter.search_recent(query, 10)
    user_info, twitter_info, sentiment_texts = parse_recent_search(res_search_recent)
    print(f"twitter user info: {user_info}\n")
    print(f"twitter info: {twitter_info}\n")
    print(f"twitter sentiment: {sentiment_texts}\n")

    # # if using args when running
    '''
    args = get_args()
    res_search_count = twitter.search_count(args.query, args.granularity)
    time_counts = parse_search_count(res_search_count)
    print(f"twitter count in last 8 time slots: {time_counts}\n")
    res_search_recent = twitter.search_recent(args.query, args.res_number)
    user_info, twitter_info, sentiment_texts = parse_recent_search(res_search_recent)
    print(f"twitter user info: {user_info}\n")
    print(f"twitter info: {twitter_info}\n")
    print(f"twitter sentiment: {sentiment_texts}\n")
    '''
