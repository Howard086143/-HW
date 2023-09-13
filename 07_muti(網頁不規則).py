"""pyETL class practing worn for biojob ptt(多頁,且網址沒有規律變化)"""

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Bio-Job/index.html"

headers = {
    "User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


for _ in range(5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text,"html.parser")

    title_tag_list = soup.select('div.title a')

    # print(title_taq_list)

    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.ptt.cc" + title_tag["href"]
        print(title)
        print(article_url)

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
    # print(new_url)
    #https://www.ptt.cc/bbs/Bio-Job/index683.html 上一頁的網址



