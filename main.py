import xml.etree.ElementTree as ET

all_txt = []
tree = ET.parse('newsafr.xml')
root = tree.getroot()
news_all = root.findall('channel/item')

for news in news_all:
    description = news.find('description')
    description = description.text.split(' ')
    all_txt += description
# print(all_txt)
long_words = []
for word in all_txt:
    # print(word)
    if len(word) > 6:
        long_words.append(word)


set_long_words = set(long_words)

list = []
top = []

for word in set_long_words:
    number_of_repeats = long_words.count(word)
    list.append([word, number_of_repeats])

list.sort(key = lambda file: file[1], reverse=True)
for word in list[:10]:
    top.append(word[0])

print(top)