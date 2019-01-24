from bs4 import BeautifulSoup, NavigableString

import requests


def strip_html(src):
    p = BeautifulSoup(src)
    text = p.findAll(text=lambda text: isinstance(text, NavigableString))

    return u" ".join(text)


lst = []
thisList = ['https://www.nytimes.com/2019/01/16/technology/huawei-investigation-trade-secrets.html',
            'https://www.nytimes.com/2019/01/22/technology/huawei-europe-china.html'
            ]


for i in thisList:
    lst.append(requests.get(i))

for k in lst:

    a = BeautifulSoup(k.text, 'html.parser')
    f = open("file_" + a.title.string + ".txt", "w")
    f.write(a.title.string)
    f.write("\n\n\n\n\n")
    for e in a.findAll(True, {"name": ["articleBody"]}):
        if e.name in "section":
            f.write(e.get_text())
