import re
import os
import jieba


class Text(object):
    def __init__(self, text_route):
        self.text_route = text_route

    def get_size(self):
        return os.path.getsize(self.text_route)

    def get_word_list(self, num=0):
        with open(self.text_route, 'r', encoding='utf-8') as file:
            text = file.read()
        if num == 1:
            res = re.compile(r"([\u4e00-\u9fa5])")  # 正则包根据单个中文文字分割字符串
            text_list_init = res.split(text)
        else:
            text_list_init = jieba.lcut(text)  # jieba包根据词语分割字符串
        text_list_result = []
        for literacy in text_list_init:
            if '\u4e00' <= literacy <= '\u9fa5':  # 除去非中文的列表元素
                text_list_result.append(literacy)
        return text_list_result
