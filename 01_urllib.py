from urllib import request

url = "https://www.104.com.tw/jobs/main/"

res = request.urlopen(url=url)

html = res.read().decode("utf-8")

print(html)


