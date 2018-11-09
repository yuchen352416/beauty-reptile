#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import logging as log



def get_image_list(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    log.info("成功获取图片列表...")
    obj = json.loads(response.text)
    arr = obj.get("data")
    log.info("正在解析数据...")
    for item in arr:
        # print(item)
        print(item.get("image_count"))

def run():
    for i in range(10):
        page_size = 20
        offset = i * page_size
        url = "https://www.toutiao.com/search_content/?format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&cur_tab=3&from=gallery&offset={0}".format(offset)
        get_image_list(url)





if __name__ == "__main__":
    log.getLogger().setLevel(log.INFO)
    run()

