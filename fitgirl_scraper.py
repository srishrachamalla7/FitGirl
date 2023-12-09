import html
import requests
from bs4 import BeautifulSoup
import re


url= "https://fitgirl-repacks.site/feed/"
response=requests.get(url)
soup=BeautifulSoup(response.content,'xml')

main=soup.find("item")
date=main.pubDate.text

com=main.find("content:encoded")
for i in com:
  pp=i.text

cp = []
pattern = r"\⇢ (.+?)</span>"
index = 0

while True:
  match = re.search(pattern, pp[index:])

  if match:
    cp.append(match.group(1))
    index += match.end()
  else:
    break
# remove the unnecessary
cp=cp[0:-2]

upcoming_repacks=cp

s=soup.findAll('description') 

title_pattern= '<p>(.+?)Genres'
genre_pattern= "Genres/Tags: (.+?)Companies"
company_pattern= "Companies: (.+?)Language"
org_size_pattern= "Original Size: (.+?) Repack"
rpk_size_pattern= "Repack Size: (.+?) Download"
href_pattern= '<a href="(.+?)" cl' 
Languages_pattern= '(?:Language|Languages): (.+?) Original'

for i in s:
    z = i.text

    # Extract title
    if re.search(title_pattern, z):
        result4 = re.search(title_pattern, z).group(1).strip()
        cmpl = result4
        print(html.unescape(cmpl))
        titles.append(html.unescape(cmpl))

    # Extract genres
    if re.search(genre_pattern, z):
        genres = re.search(genre_pattern, z).group(1).strip()
        print(genres)

    # Extract companies
    if re.search(company_pattern, z):
        companies = re.search(company_pattern, z).group(1).strip()
        print(companies)

    # Extract original size
    if re.search(org_size_pattern, z):
        org_size = re.search(org_size_pattern, z).group(1).strip()
        print(org_size)

    # Extract repack size
    if re.search(rpk_size_pattern, z):
        rpk_size = re.search(rpk_size_pattern, z).group(1).strip()
        print(rpk_size)

    # Extract href
    if re.search(href_pattern, z):
        href = re.search(href_pattern, z).group(1).strip()
        print(href)

    # Extract languages
    if re.search(Languages_pattern, z):
        languages = re.search(Languages_pattern, z).group(1).strip()
        print(languages)

  
print("Upcoming Repacks:")
for repack in upcoming_repacks:
    print(repack)
