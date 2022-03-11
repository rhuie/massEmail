from turtle import home
import requests
from bs4 import BeautifulSoup
from home import makehome
import pyperclip


response = requests.get(
    'https://www.ashlandauction.com/auctions?page=1&pageSize=120&search=&sort=null&currentDisplay=tile&websiteDisplay%5B0%5D=tile&websiteDisplay%5B1%5D=map&websiteDisplay%5B2%5D=calendar&canToggle=true')
# print(response.text)
parser = BeautifulSoup(response.text, 'html.parser')
grid = parser.find("div", class_="view-tile")
auctions = grid.findAll("div", class_="auction")
allHomes = ''
count = 0
for auction in auctions:
    count += 1
    if count == 10:
        break
    title = auction.find("p", class_="auctionTitle").text
    startingBid = auction.findAll("div", class_="value")[0].text
    initialDeposit = auction.findAll("div", class_="value")[1].text
    imageTag = auction.find(
        "div", class_="auctionImageTag").text
    preAuction = auction.find(
        "div", class_="tile-description").contents[1].text.strip()
    auctionDetailsList = auction.find(
        "div", class_="tile-description").contents[6].text.split(' ')[1:4]
    auctionDetailsList[1] += auctionDetailsList.pop()
    auctionDetailsString = " @ ".join(auctionDetailsList)
    imageSrc = auction.find('img')['src'].replace('medium', 'medium')
    auctionLink = auction.find('a')['href']
    options = {
        'title': title,
        'startingBid': startingBid,
        'initialDeposit': initialDeposit,
        'imageTag': imageTag,
        'preAuction': preAuction,
        'auctionDetailsString': auctionDetailsString,
        'auctionLink': auctionLink,
        'imageSrc': imageSrc
    }
    # print(options['imageSrc'])
    allHomes += makehome(options)
print(allHomes)
pyperclip.copy(allHomes)
#print(f'title: {title} startingbid: {startingBid} initial deposit: {initialDeposit} image tag: {imageTag} Pre-Auction Offers: {preAuction} ends at: {auctionDetailsString} image source: {imageSrc} auction link: {auctionLink} \n')


# results.find("div", class_="card-content")
