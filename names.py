import urllib.request
import requests
import re
import string
all_of_them = []
for s in string.ascii_uppercase[:26]:
    x = requests.get('https://www.looktamil.com/babynames/show/names/letter/'+s, verify=False).text
    title_search = re.findall("<span id=\"babyNameshowBlue\">([a-zA-Z]+).*?</span>", x)
    all_of_them = all_of_them + title_search
print(all_of_them)
print(len(all_of_them))
less_than_seven = []
for name in all_of_them:
    if len(name) == 8:
        less_than_seven += [name]

print(less_than_seven)
print(len(less_than_seven))


