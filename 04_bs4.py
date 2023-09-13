import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Bio-Job/index.html"

headers = {
    "User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

# print(res.text)

soup = BeautifulSoup(res.text)

# print(soup)

title_taq = soup.find_all('a',{'id':'logo'})
title_taq = soup.find_all('a',id='logo')
# 兩者結果相同

title_taq = soup.find('a',{'id':'logo'})   #<a href="/bbs/" id="logo">批踢踢實業坊</a> 只抓第一個a標籤

print(title_taq)

# select

title_taq = soup.select('a[id="logo"]')     #效果前面
title_taq = soup.select('a#logo')
# title_taq = soup.select_one('a#logo')       #回傳第一個標籤

print(title_taq)
print(title_taq[0])
print(title_taq[0].text)  #抓出[<a href="/bbs/" id="logo">批踢踢實業坊</a>] 的 批踢踢實業坊
print("https://www.ptt.cc" + title_taq[0]["href"])  #加上連結


title_taq = soup.find_all('div', class_='title')
print(title_taq)
print(title_taq[0].select_one('a').text)

