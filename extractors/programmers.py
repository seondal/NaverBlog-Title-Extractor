from requests import get
from bs4 import BeautifulSoup


def extract_programmers(link):
    result = {}
    
    response = get(f"{link}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 링크
    result['link'] = link

    # 번호
    result['id'] = link.split("/")[-1]
    result['blog_title'] = f"[프로그래머스][SQL] "

    # 제목
    span_tag = soup.find("span", class_="challenge-title")
    if span_tag:
        result['title'] = span_tag.string.strip()
        result['blog_title'] += f"{result['title']} ({result['id']})"

        
    # 문제
    h5_tag = soup.find("h5", text="문제")
    if h5_tag:
        contents = []
        next_tag = h5_tag.find_next_sibling()

        while next_tag and next_tag.name != 'hr':  # <hr/> 태그가 나오기 전까지의 모든 <p> 요소를 추출
            if next_tag.name == 'p':
                contents.append(next_tag.get_text())  # <p> 태그의 텍스트 추출
                next_tag = next_tag.find_next_sibling()  # 다음 형제 요소로 이동

        result['content'] = contents

    return result
