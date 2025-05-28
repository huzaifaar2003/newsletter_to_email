import requests

API_KEY = "31a91e4e6dd24e138b4c7edb7b32e305"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-04-28&sortBy=publishedAt&apiKey=31a91e4e6dd24e138b4c7edb7b32e305"

# adding a headers varible to put inot the requests.get() as the "headers" argument value
# did that since I was getting a return of "Edge: Too Many Requests"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# make request
request = requests.get(url, headers=headers)
# extract the content from the url in a .json format so that it is more usable
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["content"])
    print("\n")