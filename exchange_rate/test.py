'''import mechanicalsoup

# Create a browser object
browser = mechanicalsoup.StatefulBrowser()

# Open the website
url = "https://www.bankofabyssinia.com/exchange-rate-2/"
browser.open(url)

# Find the table by its class name
table_class = "tablepress tablepress-id-15 dataTable no-footer"
table = browser.select(f".{table_class}")[0]

# Extract the table data into a list
table_data = []
for row in table.select("tr"):
    row_data = [cell.text for cell in row.select("th, td")]
    table_data.append(row_data)

# Print the table data
for row in table_data:
    print(row)
'''
#This will not run on online IDE
import requests
from bs4 import BeautifulSoup

URL = "https://www.bankofabyssinia.com/exchange-rate-2/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
print(type(soup))
table = soup.find(id='tablepress-15')
print(type(table))

table_body = table.find('tbody')
rows = table_body.find_all('tr')
print(type(rows))
for r in rows:
    data = r.find_all('td')
    for d in data:
        if d.text == "USD":
            print(d.text)
