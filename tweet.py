'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import statistics
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity = []
subjectivity = []
# Continue your program below!
# Textblob sample:
ls = [[], []]
for each in tweetData:
    tb = TextBlob(each["text"])
    polarity.append(tb.polarity)
    release= sum(polarity)/len(polarity)
    subjectivity.append(tb.subjectivity)
    releases= sum(subjectivity)/len(subjectivity)
print("Average of polarity=", release)
print("Average of ubjectivity=", releases)

num_bins = 5
n, bins, patches = plt.hist(polarity, num_bins, facecolor = 'pink', alpha = 0.75)
plt.show()

n, bins, patches, = plt.hist(subjectivity, num_bins, facecolor = "maroon", alpha = 0.5)
plt.show()

def word_cloud_freq(tweetData):
    all_text = ""
    word_count = {}
    for each in tweetData:
        all_text += each["text"]
    all_text = all_text.lower()
    atb = TextBlob(all_text)
    word_list = atb.words
    for each in word_list:
        if len(each) > 3 and each.isalpha() == True and each != "https":
            if each not in word_count:
                word_count[each] = 1
            else:
                word_count[each] += 1
    wc = WordCloud(background_color="white", width=900, height=500,
    relative_scaling=1).generate_from_frequencies(word_count)
    plt.imshow(wc, interpolation='bilinear')
    plt.show()
word_cloud_freq(tweetData)

# Combined word cloud
word_cloud_freq(tweetData)
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)
print(statistics.mean(ls[1]))
print(statistics.mean(ls[0]))
