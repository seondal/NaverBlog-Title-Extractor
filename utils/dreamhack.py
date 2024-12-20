from requests import get
from bs4 import BeautifulSoup

tag_dictionary = {
    "web" : "웹해킹",
    "reversing" : "리버싱",
    "pwnable" : "시스템해킹",
    "crypto" : "암호학",
    "misc" : "포렌식",
    "forensics" : "포렌식",
    "web3" : "WEB3",
    "cloud" : "클라우드",

}

def extract_dreamhack(link):
    result = {}
    
    response = get(f"{link}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    result['type'] = 'bandit'
    result['blog_title'] = f"[Dreamhack] 드림핵 "

    # 링크
    result['link'] = link

    # 제목
    info_div = soup.find("div", id="challenge-info")
    if info_div:
        title_h1 = info_div.find("h1")
        tag_span = info_div.find("span", class_="tag")
        level_span = info_div.find("span", class_="level")
        if tag_span:
            result['blog_title'] += f"{tag_dictionary[tag_span.get_text(strip=True)]} "
        if title_h1:
            result['blog_title'] += f": {title_h1.get_text()}"
        if level_span:
            result['blog_title'] += f" ({level_span.get_text()})"

    # 문제

    return result
