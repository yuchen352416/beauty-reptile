#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging as log
import re

def get_html(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except:
        # 服务器可能会出错...
        return None

def out_file(content, mode='a+'):
    file_name = "/Users/Selfimpr/development/test.txt"
    with open(file_name, mode, encoding="UTF-8") as f:
        f.write(content)

def get_article(url):
    '''
    获取小说对应章节的文章
    :param url:
    :return:
    '''
    html = get_html(url)
    if None != html:
        soup = BeautifulSoup(html, 'lxml')
        article_title = soup.find("h1", attrs={"id": "nr_title"}).text
        log.info("正在下载: {}".format(article_title))
        article_content = ""
        arr = soup.find("div", attrs={"id": "nr1"}).find_all("p")
        for i in range(0, arr.__len__()):
            article_content += "\n{}".format(arr[i].text)
        article = "\n\n{}\n{}\n".format(article_title, article_content)
        out_file(article)

def run():
    url = "http://www.luoxia.com/zetian/"
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    titles = soup.find_all("div", attrs={"class": "title clearfix"});
    chapters = soup.find_all("div", attrs={"class": "book-list clearfix"});
    for i in range(0, titles.__len__()):
        log.info("正在下载: {}".format(titles[i].text))
        out_file(titles[i].text)
        arr = chapters[i].find("ul").find_all("li")
        for j in range(0, arr.__len__()):
            regex = "(http://www.luoxia.com/zetian/\d+\.htm)"
            article_url = re.search(regex, arr[j].__str__()).group(1)
            get_article(article_url)

if __name__ == "__main__":
    log.getLogger().setLevel(log.INFO)
    run()
