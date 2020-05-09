import urllib.request
import requests
import re
import string
all_of_them = []
for s in range(1, 67):
    x = requests.get("https://www.prokerala.com/kids/baby-names/hindu/boy/page-"+str(s)+".html", verify=False).text
    title_search = re.findall('<a data-event-track=\"click:ab\.baby-names\.name-detail-page\" href=\".*?\">(.+)<\/a>', x)
    print(title_search)
    all_of_them = all_of_them + title_search
print(all_of_them)
print(len(all_of_them))

for name in all_of_them:
    print(name)
