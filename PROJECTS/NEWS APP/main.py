import requests

query="artificialintelligence" #as for query take user input word then you can just make it like search bar
api="8e72024b754f4ab18a949a9715b4577a"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-09-02&sortBy=publishedAt&apiKey={api}"

print(url)

r=requests.get(url)

data=r.json()

articles= data["articles"]

for article in articles:
    print(article["title"])
    print("////")
    print(article["url"])
    print("******************")