"""
Author : Bigdimuss
Description : QWant Api Client

"""

import requests

headers = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

class SessionType:
    normal = "normal"
    junior = "junior"
    
class Qwant_Api:
    
    _api_link = {
    SessionType.normal:{
        "search":"https://api.qwant.com/v3/search/web",
        "knowledge":"https://api.qwant.com/v3/ia/knowledge2",
        "news" : "https://api.qwant.com/v3/search/news",
        "images" : "https://api.qwant.com/v3/search/images", ##### ADD MORE PARAMS #####
        "videos": "https://api.qwant.com/v3/search/videos",
        "shopping":"https://api.qwant.com/v3/search/shopping",},
    SessionType.junior:{
        "search":"https://api.qwant.com/v3/egp/search/web",
        "images" : "https://api.qwant.com/v3/egp/search/images", ##### ADD MORE PARAMS #####
        "videos": "https://api.qwant.com/v3/egp/search/videos"
    }}
    
    def __init__(self, headers:dict=headers, session_type:str=SessionType.normal):
        self.headers = headers
        self.session = requests.session()
        self.session.headers = self.headers
        self.session_type = session_type
        
    def get_search(self,
                   q:str,
                   freshness:str='all',
                   locale:str='fr_FR',
                   offset:int=0,
                   safesearch:int=1):
        params = {'q': q,
                  'freshness':freshness,
                  'count': 10,
                  'locale': locale,
                  'offset': offset,
                  'device': 'desktop',
                  'safesearch': safesearch}
        
        url = self._api_link.get(self.session_type).get("search")
        result = self.session.get(url=url,
                                  params=params)
        
        if result.status_code == 200:
            return result.json()
        else:
            return None
    
    def get_knowledge(self,
                      q:str,
                      locale:str='fr_FR',
                      tgp:int=50) -> dict:
        
        params = {'q': q, 'locale': 'fr_fr', 'tgp': tgp,}
        url = self._api_link.get(self.session_type).get('knowledge')
        result = self.session.get(url = url,
                                  params = params)
        if result.status_code == 200:
            return result.json()
        else:
            return None

    def get_news(self,
                 q:str,
                 freshness:str='all',
                 source:str='all',
                 order:str='relevance',
                 locale:str='fr_FR',
                 offset:int= 0,
                 safesearch:int=1) -> dict:
        
        #order : relevance, date
        #freshness : hour, day, week, month
        
        params = {'t':'news',
                  'q':q,
                  'freshness':'all',
                  'source':source,
                  'order':order,
                  'count':10,
                  'locale':locale,
                  'offset':offset,
                  'device':'desktop',
                  'safesearch':safesearch,}
        
        if self.session_type == SessionType.normal:
            url = self._api_link.get(self.session_type).get("news")
            result = self.session.get(url=url, params=params)
            return result.json()
        
        else:
            return None
        
    def get_images(self,
                   q:str,
                   freshness:str='all',
                   size:str='all',
                   imagetype:str='all',
                   license:str='all',
                   color:str='all',
                   locale:str='fr_FR',
                   offset:int=0,
                   safesearch:int=1) -> dict:
    
        params = {'t':'images',
                  'q':q,
                  'freshness':freshness,
                  'size':size,
                  'imagetype':imagetype,
                  'license':license,
                  'color':color,
                  'count':50,
                  'locale':locale,
                  'offset':offset,
                  'device':'desktop',
                  'safesearch':safesearch,}
        url = self._api_link.get(self.session_type).get("images")
        result = self.session.get(url=url, params=params)
        if result.status_code == 200:
            return result.json()
        else:
            return None
        
    def get_shopping(self,
                     q:str,
                     locale='fr_FR',
                     safesearch:int=1,
                     tgp:int=80) -> dict:
        params = {'t':'shopping',
                  'q':q,
                  'locale':locale,
                  'device':'desktop',
                  'safesearch':1,
                  'tgp':80,}
        
        url = self._api_link.get(self.session_type).get("shopping")
        result = self.session.get(url=url, params=params)
        if result.status_code == 200:
            return result.json()
        else:
            return None
    
    def get_videos(self,q:str,
                  source:str='all',
                  order:str='relevance',
                  locale:str='fr_FR',
                  offset:int=0,
                  safesearch:int=1) -> dict:
    # order : relevance, view, date
        params = {'t':'videos',
                  'q':q,
                  'source':source,
                  'order':order,
                  'count':10,
                  'locale':locale,
                  'offset':offset,
                  'device':'desktop',
                  'safesearch':safesearch}
        
        url = self._api_link.get(self.session_type).get("videos")
        result = self.session.get(url=url, params=params)
        if result.status_code == 200:
            return result.json()
        else:
            return None
  
if __main__ == 'main':
  q = Qwant_Api()
  search = q.get_search('Your Search Words')
  print(search)
