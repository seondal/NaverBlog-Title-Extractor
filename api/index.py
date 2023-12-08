from flask import Flask, render_template, request
from extractors.blog import extract_blog_title

app = Flask("Naver Blog Title Extractor")


@app.route("/")
def home():
  if "link" in request.args:
    link = request.args.get("link")

    splitted_link = link.split("/")

    blog_id = splitted_link[3]
    log_no = splitted_link[4]

    post_url = f"https://blog.naver.com/PostView.naver?blogId={blog_id}&logNo={log_no}&redirect=Dlog&widgetTypeCall=true&directAccess=false"

    data = extract_blog_title(post_url)

    return render_template("result.html", link=link, data=data)

  else:
    return render_template("home.html")
  