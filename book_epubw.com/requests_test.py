import requests

response = requests.get("https://sobooks.cc/books/15702.html")
html = response.text
print(html)