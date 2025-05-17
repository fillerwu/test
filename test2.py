# coding=utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud
text=open('1.txt',encoding='utf-8').read()
#mask 就是背景，这里是用数字公式绘制的要给园
wc=WordCloud(font_path="msyh.ttc").generate(text = text)
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()
wc.to_file("test.png")