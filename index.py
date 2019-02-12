#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

page_url = "https://finance.naver.com/marketindex/worldGoldDetail.nhn?marketindexCd=CMDT_GC&fdtc=2"
res = requests.get(page_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

print(soup)

section_aside = soup.find("div",{"class" : "section_aside"})

for side_section in section_aside.find_all("tr"):
    for a_search in side_section.find_all("a"):
        print(a_search)


    for td_search in side_section.find_all("td"):
        print(td_search)

i = 0
for side_section in section_aside.find_all("tr"):
    if i > 0:
        j = 1
        for a_search in side_section.find_all("a"):
            if j == 1:
                title = a_search.text.strip()
            else:
                unit = a_search.text.strip()
            j = j+1

        j = 1
        for td_search in side_section.find_all("td"):
            if j == 1:
                content = td_search.text.strip()
            else:
                scope = td_search.text.strip()
            j = j+1

        updown = side_section.img.get("alt")

        # new_text = new_text + "\n" + title + " - " + unit + " = " + content + " : " + scope + updown
        print(title + " - "+ unit + " = " + content + " : " + scope + updown)
        # print(new_text)
    i = i+1

# print(new_text)

# f = open("index_report.txt","a")
# f.write(new_text)
# f.close()

# with open("worldgold_report.txt","a") as f:
#     f.write(new_text)