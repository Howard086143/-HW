"""Homework for 104 job search"""

import requests
from bs4 import BeautifulSoup
from crawler_nuits_104 import load_artical_to_some_folder

url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%E5%B8%AB%20Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=2&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"

headers = {
    "User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


for _ in range(10):
    res = requests.get(url, headers=headers, timeout=60)

    soup = BeautifulSoup(res.text,"html.parser")

    title_tag_list = soup.select('div.title a')

    # Get artical title, url, and content. load to Text.
    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.104.com.tw/" + title_tag["href"]
        print(title)
        print(article_url)

    #存下文章
    try:
        load_artical_to_some_folder(
            artical_url=article_url,
            file_name=title.replace("/"," ")
        ) 
    except OSError as e:
        print(e)    
    except Exception as e:
        print(e)

    url = "https://www.104.com.tw/" + soup.select('a[class="btn wide"]')[1]["href"]
    # print(new_url)
    #https://www.ptt.cc/bbs/Bio-Job/index683.html 上一頁的網址