from flask import Flask, render_template, request, send_from_directory

from utils.blog import extract_blog_title
from utils.programmers import extract_programmers
from utils.boj import extract_boj
from utils.bandit import extract_bandit
from utils.dreamhack import extract_dreamhack

app = Flask("네이버 블로그 목차 생성기")

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/")
def blog():
  if "link" in request.args:
    link = request.args.get("link")
    
    if not link.startswith("https://blog.naver.com/"):
      return render_template("error.html", message="https://blog.naver.com/로 시작하는 올바른 네이버 블로그 글 링크를 입력해주세요")

    splitted_link = link.split("/")

    blog_id = splitted_link[3]
    log_no = splitted_link[4]

    post_url = f"https://blog.naver.com/PostView.naver?blogId={blog_id}&logNo={log_no}&redirect=Dlog&widgetTypeCall=true&directAccess=false"

    data = extract_blog_title(post_url)

    return render_template("blog.html", link=link, data=data)

  else:
    return render_template("blog.html")

@app.route("/ps", methods=['GET', 'POST'])
def ps():
  LANGUAGES = ["None","JavaScript","PHP","Java","Golang","Python","C#","C++","Erlang"]

  if "link" in request.args and "lang" in request.args:
    lang = request.args.get("lang")
    link = request.args.get("link")

    if link.startswith("https://www.acmicpc.net/problem/"):
      data = extract_boj(link, lang)
      return render_template("ps.html", langs=LANGUAGES, link=link, data=data, language=lang)
    elif link.startswith("https://school.programmers.co.kr/"):
      data = extract_programmers(link, lang)
      return render_template("ps.html", langs=LANGUAGES, link=link, data=data, language=lang)
    elif link.startswith("https://overthewire.org/wargames/bandit/"):
      data = extract_bandit(link)
      return render_template("ps.html", link=link, data=data)
    elif link.startswith("https://dreamhack.io/wargame/challenges/"):
      data = extract_dreamhack(link)
      return render_template("ps.html", link=link, data=data)
    else:
      return render_template("error.html", message="현재 프로그래머스(https://school.programmers.co.kr/), 백준(https://www.acmicpc.net/problem/), 드림핵(https://dreamhack.io/wargame/challenges/), Bandit(https://overthewire.org/wargames/bandit/) 문제 링크만 가능합니다. 추가하고싶은 플랫폼이 있다면 제작자에게 문의해주세요!")
  
  else:
    return render_template("ps.html", langs=LANGUAGES)

@app.route("/test/ps")
def test_ps():
  if "link" in request.args and "lang" in request.args:
    lang = request.args.get("lang")
    link = request.args.get("link")

    if link.startswith("https://www.acmicpc.net/problem/"):
      data = extract_boj(link, lang)
      return data
    elif link.startswith("https://school.programmers.co.kr/"):
      data = extract_programmers(link, lang)
      return data
    else:
      return "에러페이지"   
  else:
    return "기본페이지"