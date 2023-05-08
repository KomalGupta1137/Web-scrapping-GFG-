import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/python-programming-language/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
pandaDiv = soup.find('div', class_='Pandas')
pandaList = pandaDiv.find_all('li')
scrappedData = [{"links":"", "title":""}]


for anchor in pandaList:
    list = anchor.find('a')
    href = list.get('href')
    text = list.text
    scrappedData.append({
        "links":href,
        "title":text
    })
print(scrappedData)   


   
