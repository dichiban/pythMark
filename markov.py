from collections import defaultdict
import re
import random

# Text file to string.
with open("C:/home/pythMark/texts/sherlock.txt") as f:
    text = f.read().lower()

text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
word = set(words)
word_dict = defaultdict(list)

for i, w in enumerate(words):
    if i < len(words) - 1:
        word_dict[w].append(words[i+1])

initial = random.randint(0, len(words))
current = words[initial]
sentence = [words[initial]]

for i in range(0, 10):
    sentence.append(word_dict[current][random.randint(0,len(word_dict[current])-1)])
    current = word_dict[current][0]

print(sentence)