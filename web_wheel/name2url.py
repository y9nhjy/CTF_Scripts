import time
from time import sleep

from bs4 import BeautifulSoup
from lxml import etree
import requests


def schoolname(url):
    with open('names.txt', 'w') as f:
        for i in range(1, 100):
            sleep(1)
            pageurl = url + str(i)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Referer': 'https://www.google.com/',
                'Accept-Language': 'en-US,en;q=0.9',
                'Authorization': 'Bearer your_token_here'
            }
            req = requests.get(pageurl, headers=headers)
            # print(req)
            tree = etree.HTML(req.text)
            res = tree.xpath('//td[@class="am-text-center"]/a/text()')
            for j in res:
                f.write(j + '\n')
            # print("爬取 %s" % res)


# schoolname('https://src.sjtu.edu.cn/rank/firm/0/?page=')

def search_university_website(query):
    # time.sleep(1)
    url = f"https://www.bing.com/search?q={query}+官网"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = soup.find_all('div', class_='b_attribution')
    if results:
        link = results[0].find('cite').text
        return link
    else:
        return None

def get_university_websites(filename):
    with open(filename, 'r', encoding='gbk') as file:
        universities = file.readlines()
        universities = [uni.strip() for uni in universities]

    university_websites = {}
    for university in universities:
        website = search_university_website(university)
        university_websites[university] = website

    return university_websites

filename = 'names.txt'
websites = get_university_websites(filename)

with open('urls.txt', 'w') as f:
    for university, website in websites.items():
        if website is not None:
            f.write(f"{website}\n")
            # print(f"{university}: {website}")

# file = open('names.txt', 'r')
# urls = file.readlines()
# for url in urls:
#     url = url.strip()
#     try:
#         url += "paylaod"
#         r = requests.get(url, timeout=1)
#         r.encoding = r.apparent_encoding
#         HtmlText = r.text
#         if '0day' in HtmlText:
#             print(url)
#         else:
#             pass
#     except:
#         pass
