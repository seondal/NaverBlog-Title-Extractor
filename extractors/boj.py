from requests import get
from bs4 import BeautifulSoup

def extract_boj(link): 
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    response = get(f"{link}", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    result = {}

    # 링크
    result['link'] = link

    # 번호
    result['id'] = link.split("/")[-1]
    result['blog_title'] = f"[BOJ][C++] 백준 {result['id']}번: "

    # 제목
    span_tag = soup.find("span", id="problem_title")
    if span_tag:
        result['title'] = span_tag.string.strip()
        result['blog_title'] += result['title']
        
    # 문제
    problem_div = soup.find("div", id="problem_description")
    if problem_div:
        p_tags = problem_div.find_all("p")  # <p> 요소들을 리스트로 가져옴
        contents = [p.get_text(strip=True) for p in p_tags] # 각 <p> 요소의 텍스트 추출
        result['content'] = contents

    return result
