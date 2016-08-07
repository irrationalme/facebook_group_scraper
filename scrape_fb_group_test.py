import requests
import json
import re

access_token = 'EAACEdEose0cBAD0xqJ4xAjyefN4tdesLSfRkNqX0c5bviKOPEYEYfnLocJofndJOJd6BoZCmWGQIE1RRhyu8aCzsdkKKC5ip4ph3TpcD9VospY0w3mHbfQ8BRP0vpl4ZBZB1K12HdTZAeYW6sqZC7ZAr98cfjZAZCZAmwD9BaSFTVnAZDZD'
group_id = '1099938296713514'
uid_menno = '10204615074563611'

base_url = 'https://graph.facebook.com/v2.3'
node = '/' + group_id
arguments = '?fields=feed'

url = base_url + node + arguments + '&access_token=' + access_token

req = requests.get(url)
raw_data = req.json()
feed = raw_data['feed']['data']

next_url = raw_data['feed']['paging']['next']

for topic in feed:
    if topic['from']['id'] == uid_menno:
        topic_message = topic['message']
        link = topic['actions']
