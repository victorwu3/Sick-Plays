from pprint import pprint

import requests

import json
import praw

import pdb
#
# r = requests.get(r'http://www.reddit.com/r/nba/new.json?sort=hot')
#
# data = r.json()
#
# pdb.set_trace()
# print(data)
#
#
reddit = praw.Reddit(client_id='O0r4WVJ1VWL7TA',
                     client_secret='8oVSvH15EVK-2hQ5T5ljDcghXKI',
                     password='Vw110594',
                     user_agent='sickplays by /u/snipedbyanasian',
                     username='snipedbyanasian')

print(reddit.user.me())
