import requests



url = "https://www.104.com.tw/jobs/main/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

data = {
    "username":""

}

res = requests.post(url, data=data, headers=headers)

print(res.text)