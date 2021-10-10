# -*- coding:utf-8 -*-
"""
@author:starlee
@file:ciyun.py
@time:2021/6/1116:13
"""

from wordcloud import WordCloud
# from scipy.misc import imread
from imageio import imread
import matplotlib.pyplot as plt
import jieba

def read_deal_text():
    with open("腰部_132981_7.25.txt", "r") as f:  # 读取我们的待处理本文
        txt = f.read()

    re_move = ["，", "。", '\n', '\xa0']  # 无效数据
    # 去除无效数据
    for i in re_move:
        txt = txt.replace(i, " ")
    word = jieba.lcut(txt)  # 使用精确分词模式进行分词后保存为word列表

    with open("txt_save.txt", 'w') as file:
        for i in word:
            file.write(str(i) + ' ')
    print("文本处理完成")

def img_grearte():
    mask = imread("pic.jpg")
    with open("txt_save.txt", "r") as file:
        txt = file.read()
    word = WordCloud(background_color="white", \
                     width=800, \
                     height=800,
                     font_path='simhei.ttf',
                     mask=mask,
                     ).generate(txt)
    word.to_file('test.png')
    print("词云图片已保存")

    plt.imshow(word)  # 使用plt库显示图片
    plt.axis("off")
    plt.show()

read_deal_text()
img_grearte()