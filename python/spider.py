import re

import requests
import bs4

header = {
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'en-US,en;q=0.9,zh-CN',
    # 'cache-control': 'no-cache',
    # 'connection': 'keep-alive',
    # 'host': 'www.douban.com',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}


def download_page(url):
    """

    download all the pages
    """
    page_obj = requests.get(url, headers=header)
    bs4_obj = bs4.BeautifulSoup(page_obj.text, 'lxml')
    # download all the page
    url_set = set()
    paginator = bs4.find("div", attrs={"class": "paginator"})
    if paginator:
        for a_ele in paginator.find_all("a"):
            url_set.add(a_ele.attrs.get("href"))

        bs4_page_obj_list = [bs4_obj]
        for url in url_set:
            print(f"download_pages{url}" )
            page_obj = requests.get(url, headers=header)
            bs4_page_obj = bs4.BeautifulSoup(page_obj.text, "lxml")
            bs4_page_obj_list.append(bs4_page_obj)
    return bs4_page_obj_list

download_page("https://movie.douban.com/subject/35593344/")
# fetch all the email
# comment_all = bs4_obj.find("div", attrs={"class": "short-content"})
# print(comment_all)
# for all in comment_all:
#     comment_all = all.find("p", attrs == {"class": "reply-content"})
#     email_addr = re.search("\w+@\w+.\w+", comment_all.text, flags=re.A)
#     if email_addr:
#         pub_time = all.find("span", attrs={"class": "pub-time"})
#         print(email_addr.group(), pub_time.text)
