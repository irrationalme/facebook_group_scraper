import requests
import re
import sys
import sqlite3


access_token = 'EAACEdEose0cBANgiLGYiNu9EuNsS65U6HQ8XwMEbjFhkZCbSbQ0JgVZC9qZAviG5GggweqnBZAQYiIooZAIUoKuCqGAkVoVdMdhaz0b3prSB0PLEGt8ZCJI38SwYCbBGVyPQgw3aue2M6t6qeFxAl3ZBqZC31kWk5GZBcR9C8xh12ogZDZD'
group_id = '1099938296713514'
uid_menno = '10204615074563611'

base_url = 'https://graph.facebook.com/v2.3'
node = '/' + group_id
arguments = '?fields=feed'

url = base_url + node + arguments + '&access_token=' + access_token


def get_topics():
    request = requests.get(url)
    if request.status_code == 200:
        response = request.json()
        feed = response['feed']

        try:
            while feed['paging']['next']:
                for topic in feed['data']:

                    # Filter out topics that were started by Menno
                    if topic['from']['id'] == uid_menno and '#' in topic['message'].encode('utf-8'):
                            message = topic['message'].encode('utf-8')
                            topic_id = topic['id']
                            link = topic['actions'][0]['link']
                            comments = topic['comments']
                            print link, topic_id, message, comments, '\n'

                next_url = feed['paging']['next']
                request = requests.get(next_url)
                response = request.json()
                feed = response
        except KeyError:
            sys.exit()

    else:
        sys.exit("Access token expired")


if __name__ == '__main__':
    get_topics()


# pattern = '(\#[^ ]+) - ([^:]+)'
