from requests import get
from bs4 import BeautifulSoup

def get_refined_text(div):
    text = ""
    for p in div:
        if p.name == 'p':
            text += f"{p.get_text(strip=True)}\n"
    return text


def extract_boj(link): 
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    response = get(f"{link}", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    result = {}
    result['type'] = 'boj'

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
        result['content'] = get_refined_text(problem_div)

    # 입출력
    input_div = soup.find("div", id="problem_input")
    if input_div:
        result['input'] = get_refined_text(input_div)
    output_div = soup.find("div", id="problem_output")
    if output_div:
        result['output'] = get_refined_text(output_div)


    return result