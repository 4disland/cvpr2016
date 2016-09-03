#!/usr/bin/env python
# coding=utf-8

import glob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_list = glob.glob('./fields/*.txt')


# get all the paper title and store as one single string
all_title_str = ''
for f in file_list:
    with open(f, 'r') as cur_file:
        count = 0
        for line in cur_file.readlines():
            if count % 3 == 0: # get paper title from file f
                all_title_str += line[:-1] # remove \n
            count += 1


# generate a word cloud image
wordcloud = WordCloud(width=800, height=600, background_color='white').generate(all_title_str)


# display the generated image
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('hot_topic1_white.png')
plt.show()