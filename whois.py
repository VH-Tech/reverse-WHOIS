import requests
from bs4 import BeautifulSoup

name = input("individual/organization name or e-mail address : ")  # Get name to search for

URL = "https://viewdns.info/reversewhois/?q=" + name

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
r = requests.get(URL, headers=headers)  # GET request with user headers

soup = BeautifulSoup(r.content, 'html5lib')  # parse the response data with a parser

table = soup.findAll('table')[3].encode()  # find all occurences of table in response

soup2=BeautifulSoup(table, 'html5lib')  # Create a new soup to extract <tr> tags with help of beautiful soup
rows = soup2.findAll('tr')

# iterate over occurences of <tr>
try:
    for row in rows:
        row = str(row)
        value = row[row.index('<td>') + 4: row.index('</td>')]
        if value == "Domain Name":
            print("domain names owned by " + name + " are:")

        else:
            print(value)

except:
    print(name + " doesn't have any registered domain names")
