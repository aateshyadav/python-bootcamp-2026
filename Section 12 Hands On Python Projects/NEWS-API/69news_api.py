import requests

query = input("What type of news are you interested in today? ")

api = "30c52a2a7ab142508c33400e8ed3a45c"

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)
data = r.json()

print(data)  # Debug

if data.get("status") == "ok":
    articles = data["articles"]

    for index, article in enumerate(articles, start=1):
        print(index, article["title"])
        print(article["url"])
        print("\n" + "*" * 40 + "\n")
else:
    print("API Error:", data.get("message"))