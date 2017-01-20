import json
import re
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
from enchant import DictWithPWL
from enchant.checker import SpellChecker

my_dict = DictWithPWL("en_US", pwl="terms.dict")
chkr = SpellChecker(lang=my_dict)
result = []


def find_bad_qn(a):
    url = "https://stackoverflow.com/questions?page=" + str(a) + "&sort=active"
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html5lib")
    que = bsObj.find_all("div", class_="question-summary")
    for div in que:
        link = div.a.get('href')
        name = div.a.text
        chkr.set_text(name.lower())
        list1 = []
        for err in chkr:
            list1.append(chkr.word)
        if (len(list1) > 1):
            str1 = ' '.join(list1)
            result.append({'link': link, 'name': name, 'words': str1})


print("Please Wait.. it will take some time")
for i in range(83740, 83745):
    find_bad_qn(i)
for qn in result:
    qn['link'] = "https://stackoverflow.com" + qn['link']
for qn in result:
    print(qn['link'], " Error Words:", qn['words'])
    url = qn['link']
