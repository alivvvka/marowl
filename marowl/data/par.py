# import requests
# from bs4 import BeautifulSoup

# # comics
# url = "https://gateway.marvel.com/v1/public/comics?ts=1&apikey=915adca2cc4d0031646e45524ee155ed&hash=4cb993fbd8c6946ce9ee66df2ee19f8c"

# # character
# url = "https://gateway.marvel.com/v1/public/characters?ts=1&apikey=915adca2cc4d0031646e45524ee155ed&hash=4cb993fbd8c6946ce9ee66df2ee19f8c"

# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
# }

# req = requests.get(url, headers=headers)
# src = req.text

# with open("characters.json", "w", encoding="utf-8") as file:
#     file.write(src)


# comics
# import json

# with open('comics.json', 'r') as json_file:
#     comics_data = json.load(json_file)
#     results = comics_data["data"]["results"]


# for comics in results:
#     print(comics["title"])
#     print(comics["modified"])
#     print(comics["pageCount"])
#     print(comics["urls"][0]["url"])
#     try:
#         print(comics["creators"]["items"][0]["name"])
#     except IndexError:
#         print("Anonymous")
#     print("----------------")



# characters
# import json

# with open('characters.json', 'r') as json_file:
#     char_data = json.load(json_file)
#     results = char_data["data"]["results"]


# for comics in results:
#     print(comics["name"])
#     print(comics["modified"])
#     print(comics["thumbnail"]["path"] + "." + comics["thumbnail"]["extension"])
#     print(comics["urls"][0]["url"])
#     print("----------------")
    
