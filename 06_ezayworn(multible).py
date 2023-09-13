"""pyETL class practing worn for biojob ptt(多頁,且網址有規律變化)"""
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Bio-Job/index%s.html"

headers = {
    "User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

page = 684

for _ in range(5):        # _ = i 此時使用_,而非變數i的目的為避免佔用資源
    res = requests.get(url % (page), headers=headers, timeout=30)

    soup = BeautifulSoup(res.text,"html.parser")

    title_tag_list = soup.select('div.title a')

    # print(title_taq_list)

    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.ptt.cc" + title_tag["href"]
        print(title)
        print(article_url)

    page -= 1





