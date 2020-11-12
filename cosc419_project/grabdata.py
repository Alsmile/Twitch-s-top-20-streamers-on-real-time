# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:20:56 2020

@author: aaron
"""
import requests
import json
import jsonpath


headers = {
    'Client-ID': 'juzpxb4ut6862idxbelm9frlxbp4ry',
}
params = (
    ('broadcaster_language', 'en'),
)

class TwitchSpider(object):
    url = 'https://api.twitch.tv/helix/streams'
    
    def get_html(self):
        req = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params).json()
        return req
    
    def get_data(self, req):
        names = jsonpath.jsonpath(req, '$..user_name')
        views = jsonpath.jsonpath(req, '$..viewer_count')
        #print(names,views)
        items = []
        for name, view in zip(names, views):
            item = {'name':name, 'view':view}
            items.append(item)
        return items
    
    def refine(self, items):
        items = sorted(items, key=self.sort_seed, reverse=True)
        return items
    
    def sort_seed(self, item):
        return item['view']
    
    def go(self):
        req = self.get_html()
        items = self.get_data(req)
        items = self.refine(items)
        print(items)
        with open('repos.json', 'w', encoding='utf-8') as file_write:
            json.dump(items, file_write)
    
spider = TwitchSpider()
spider.go()
