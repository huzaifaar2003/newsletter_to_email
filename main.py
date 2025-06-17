import requests
from send_email import send_mail
topic = "tesla"
API_KEY = "31a91e4e6dd24e138b4c7edb7b32e305"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2025-04-29&sortBy=publishedAt"
       "&language=en&apiKey=31a91e4e6dd24e138b4c7edb7b32e305")

# filtered the results to only give news in English by adding "&language=en" to the url
# "q=tesla" can be changed to other subject matters of interest

# adding a headers variable to put into the requests.get() as the argument for the "headers" parameter
# did that since I was getting a return of "Edge: Too Many Requests"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# make request
request = requests.get(url)

# extract the content from the url in a .json format so that it is more usable
content = request.json()
print(content,"\n")



# extracting the 5 most recent stories' information

body = ""
for i in range(0,5):
    article = content["articles"][i]
    if article["title"] is not None:
        body = body + article["title"] \
               + "\n"  + article["description"]\
               + "\n"  + article["url"] + "\n\n"



print("Str: \n",body)


# convert string to unicode by using
# .encode() method for strings

# adding a subject to the email
final_message = f"""Subject: Your Daily Newsletter
        \n
        {body}
        """


final_message = final_message.encode('utf-8')


send_mail(message = final_message,username= "automated.huzaifaar2003@gmail.com")