from requests import get
from bs4 import BeautifulSoup

def extract_bandit(link):
    result = {}
    
    response = get(f"{link}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    result['type'] = 'bandit'
    result['blog_title'] = f"[OverTheWire][Linux] Bandit Level"

    # 링크
    result['link'] = link

    # 제목
    print(soup.prettify())
    title_h1 = soup.find("div", id="title").find("h1")
    print(title_h1)
    if title_h1:
        result['blog_title'] += title_h1.get_text()

    # 문제
    content_div = soup.find("div", id="content")
    if content_div:
        lines = content_div.get_text(separator="\n", strip=True).split("\n")
        for i, line in enumerate(lines):
            if "Commands you may need to solve this level" in line:
                keywords = ", ".join(lines[i + 1].replace(",", "").split())
                lines[i + 1] = keywords
        result['content'] = "\n".join(lines)

    return result
