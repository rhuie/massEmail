import requests
from bs4 import BeautifulSoup  # parser
# get function is apart of the requests module we imported
response = requests.get('https://lolprofile.net/leaderboards/na')
# print(response) get 200 code response for OK
parser = BeautifulSoup(response.text, "html.parser")
container = parser.find("tbody")  # this is tbody
rows = container.findAll('tr')  # returns a LIST
for row in rows:
    print(row.find("span").text)
