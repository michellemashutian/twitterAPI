import requests
import os

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")


class Twitter:

    @staticmethod
    def _bearer_oauth(r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
        # r.headers["User-Agent"] = "v2RecentTweetCountsPython"
        return r

    def search_count(self, input_query, granularity):
        """
        :param input_query:
        :param granularity:
        :return:
        """
        url = "https://api.twitter.com/2/tweets/counts/recent"
        query_params = {
            "query": input_query,
            "granularity": granularity
        }
        response = requests.request("GET", url, auth=self._bearer_oauth, params=query_params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()

    def search_recent(self, input_query, res_number):
        """

        :param start_time:
        :param input_query:
        :param res_number:
        :return:
        """
        url = "https://api.twitter.com/2/tweets/search/recent"
        query_params = {'query': input_query,
                        'tweet.fields': 'id,text,author_id,created_at,lang,public_metrics',
                        'user.fields': 'public_metrics,verified',
                        'expansions': 'author_id',
                        "max_results": res_number}
        response = requests.request("GET", url, auth=self._bearer_oauth, params=query_params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()


if __name__ == "__main__":
    twitter = Twitter()
    query = "Tesla"
    granularity = "day"  # "day" or "hour"
    result_number = 10  # range from 10 to 100
    search_count_res = twitter.search_count(query, granularity)
    search_recent_res = twitter.search_recent(query, result_number)
    print(f"res: {search_count_res}")
    print(f"res: {search_recent_res}")
