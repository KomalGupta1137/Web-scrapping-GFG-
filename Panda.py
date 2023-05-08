from selenium import webdriver
from bs4 import BeautifulSoup
import requests,csv

driver = webdriver.Firefox()
url = "https://www.geeksforgeeks.org/python-programming-language/"

#to open in browser 
driver.get(url)

#to get the response from url
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
pandaDiv = soup.find('div', class_='Pandas')
pandaList = pandaDiv.find_all('li')
scrappedData = [{"links":"", "title":""}]


for anchor in pandaList:
    anchors = anchor.find('a')
    href = anchors.get('href')
    text = anchors.text
    scrappedData.append({
        "links":href,
        "title":text
    })
print(scrappedData) 
driver.close()  
