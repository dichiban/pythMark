import re
# Text file to string.
with open("C:/home/pythMark/texts/sherlock.txt") as f:
    text = f.read().lower()

text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
word = set(words)
word_dic = dict.fromkeys(word, 0)


for w in word:
    word_dic[w] = words.count(w)

print(word_dic)



        



