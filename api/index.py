from flask import Flask, render_template, request

from extractors.blog import extract_blog_title
from extractors.programmers import extract_programmers
from extractors.boj import extract_boj

app = Flask("네이버 블로그 목차 생성기")


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
  
@app.route("/ps")
def ps():
  if "link" in request.args:
    link = request.args.get("link")

    if link.startswith("https://www.acmicpc.net/problem/"):
      data = extract_boj(link)
      return render_template("ps.html", link=link, data=data)
    elif link.startswith("https://school.programmers.co.kr/"):
      data = extract_programmers(link)
      return render_template("ps.html", link=link, data=data)
    else:
      return render_template("error.html", message="프로그래머스(https://school.programmers.co.kr/)나 백준(https://www.acmicpc.net/problem/) 문제 링크만 가능합니다")
  
  else:
    return render_template("ps.html")