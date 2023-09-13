"""pyETL class practing worn for biojob(多頁,且網址沒有規律變化,並且取得文章內容)"""

import requests
from bs4 import BeautifulSoup

from crawler_nuits import load_artical_to_some_folder

url = "https://www.ptt.cc/bbs/Bio-Job/index.html"

headers = {
    "User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


for _ in range(150):
    res = requests.get(url, headers=headers, timeout=60)

    soup = BeautifulSoup(res.text,"html.parser")

    title_tag_list = soup.select('div.title a')

    # Get artical title, url, and content. load to Text.
    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.ptt.cc" + title_tag["href"]
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

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
    # print(new_url)
    #https://www.ptt.cc/bbs/Bio-Job/index683.html 上一頁的網址



