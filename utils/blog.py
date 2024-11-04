from requests import get
from bs4 import BeautifulSoup


def extract_blog_title(link):
  results = []

  response = get(f"{link}")

  soup = BeautifulSoup(response.text, "html.parser")
  titles = soup.find_all("div", class_="se-sectionTitle")

  for title in titles:
    title_text = title.find("span")
    results.append(title_text.string.strip())
  return results
