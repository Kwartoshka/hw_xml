import xml.etree.ElementTree as ET

def read_file(file):
    tree = ET.parse(file)
    root = tree.getroot()
    news_all = root.findall('channel/item')
    return news_all

def get_txt(file):
    all_txt = []
    news_all = read_file(file)
    for news in news_all:
        description = news.find('description')
        description = description.text.split(' ')
        all_txt += description
    return all_txt

def get_long_words(file):
    words_list = []
    txt = get_txt(file)
    for word in txt:
        if len(word) > 6:
            words_list.append(word)
    return words_list

def get_repeats_of_words(file):
    unique_words = {}
    long_words = get_long_words(file)
    for word in long_words:
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] += 1
    return unique_words

def get_sorted_top(file):
    repeats = get_repeats_of_words(file)
    tuples_list = list(repeats.items())
    tuples_list.sort(key=lambda file: file[1], reverse=True)
    top = []
    for word in tuples_list[:10]:
        top.append(word[0])
    return top

top = get_sorted_top(file)
print(top)