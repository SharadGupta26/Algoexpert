from datetime import datetime
from time import localtime
import time
import requests
import threading


def execution(count) :

    #url = "https://play-preprod.iqvideo.in/v5/user/playback?bn=107&chromecast=false&appId=MOBILITY&refresh=true&cp=&os=Android&ut=PO&cl=dl&op=AIRTEL&ln=pa&lg=pa&dt=Phone&dth=true&rg=true&recInProg=false&pacp=&grace=false&appVersion=1.3.7&isDth=true&contentId=ENTERR10_MOVIE_628494275556f07b5bf74fe6&pncp=&contentStatus=&currSeg="
    '''url = "http://localhost:8383/v5/user/playback?bn=107&chromecast=false&appId=MOBILITY&refresh=true&cp=&os=Android&ut=PO&cl=dl&op=AIRTEL&ln=pa&lg=pa&dt=Phone&dth=true&rg=true&recInProg=false&pacp=&grace=false&appVersion=1.3.7&isDth=true&contentId=ENTERR10_MOVIE_628494275556f07b5bf74fe6&pncp=&contentStatus=&currSeg="

    payload={}
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'x-atv-circle': 'dl',
    'Accept': '*/*',
    'x-atv-stkn': 'MCrUHjQLY8t1sqcsl1V/z9ac/hQ2b9V5neiQ6DhWpHZVyPXyP2SiBf297Pf/9H9T',
    'x-atv-utkn': 'opXaxfLVYLu1u4RRP20:9XktDtHY0HuG3kmmDD01thGpDyo=',
    'x-org-id': 'enterr10',
    'x-atv-did': 'a224e36012685b42|Phone|Android|29|107|1.3.7',
    'x-atv-segment': '',
    'apiType': 'Automation',
    'Host': 'play-preprod.iqvideo.in',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Apache-HttpClient/4.5.9 (Java/1.8.0_241)'
    }'''
    url = "https://play-staging.iqvideo.in/v5/user/playback?appId=WEB&contentId=ENTERR10_MOVIE_628494275556f07b5bf74fe6&grace=true"

    payload={}
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://preprod-enterr10.iqvideo.in',
    'Referer': 'https://preprod-enterr10.iqvideo.in/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'play-type': 'DASH',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'x-app-id': 'WEB',
    'x-atv-auth': 'yMJJKeeN8qJRfqbofkrtTvOmes4=',
    'x-atv-customer': '404-11|DTH|1|11|5',
    'x-atv-did': '1906b20a-f685-4f0a-8cd5-ba570370ca08|BROWSER|WEBOS|10.15.7|1|1.0.0',
    'x-atv-segment': 'ATVLITE',
    'x-atv-utkn': 'opXaxfLVYLu1u4RRP20:Kf0KyOgrCG2PxHtT/liRde+hDJE=',
    'x-org-id': 'enterr10',
    'x-os-id': 'WEBOS',
    'x-version-id': '1.0.0'
    }
    #count = max
    #print('start - ', localtime)
    droppedRequests = 0
    while True and count > 0:  
        try :
            response = requests.request("GET", url, headers=headers, data=payload)
        except(ConnectionError) :
            droppedRequests += 1
        count -= 1
        print(count, response.status_code, threading.current_thread().getName())
        if response.status_code != 200 :
            
            print(response.text)
            print('start - ')
            break
    if(droppedRequests > 0) :
        print('dropped requests - ' + str(droppedRequests))

def loadTest() :
    threadCount = 0
    threads = []
    iterations = 10
    while iterations > 0 :
        iterations -= 1
        threadCount += 10
        
        for i in range(threadCount) :
            threads.append(threading.Thread(target=execution, args=(10,), name='Thread-' + str(i)))
        while threads :
            threads.pop().start()
        time.sleep(5)    
        
loadTest()
#print(response.text)
