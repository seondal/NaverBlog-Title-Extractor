from requests import get
from bs4 import BeautifulSoup

def extract_bandit(link):
    result = {}
    
    response = get(f"{link}")
    soup = BeautifulSoup(response.text, "html.parser")
    
    result['type'] = 'bandit'
    result['blog_title'] = f"[Linux]"

    # 링크
    result['link'] = link

    # 문제
    content_div = soup.find("div", id="content")
    if content_div:
        lines = content_div.get_text(separator="\n", strip=True).split("\n")
        for i, line in enumerate(lines):
            if "Commands you may need to solve this level" in line:
                keywords = ", ".join(lines[i + 1].replace(",", "").split())
                lines[i + 1] = keywords
        result['content'] = "\n".join(lines)

    # if content_div:
    #     tmp = []
    #     elements = content_div.find_all()
    #     for element in elements:
    #         tmp += element

    #     result['content'] = tmp

    return result
