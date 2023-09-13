"""crawler tools"""
import requests
from bs4 import BeautifulSoup
import os

FOLDER_PATH = "./ptt_biojobs"
os.mkdir(FOLDER_PATH)
if not os.path.exists(FOLDER_PATH):
    os.mkdir(FOLDER_PATH)


headers = {
    "User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

def load_artical_to_some_folder(artical_url: str, file_name: str) -> None:
    """Request the artical and load to file"""
    res = requests.get(artical_url, headers=headers, timeout=60)
    soup = BeautifulSoup(res.text, "html.parser")
    artical_tag = soup.select_one('div[id="main-content"]')
    

    for tag_name in ["div", "a", "span"]:
        for tag in artical_tag.select('div'):
            tag.extract()
   
   
    artical = artical_tag.text
    # print(artical_tag)
    # print(artical_tag)
    # with open("%s/%s.txt" % (FOLDER_PATH, file_name), "w", encoding="utf-8") as f:
    with open(f"{FOLDER_PATH}/{file_name}.txt", "w", encoding="utf-8") as f:
        f.write(artical)

if __name__=="__main__":
    load_artical_to_some_folder(
        "https://www.ptt.cc/bbs/Bio-Job/M.1693814201.A.DC7.html",
        "[徵才] 臺大醫院內科部血液腫瘤科誠徵研究護理師",
    )
