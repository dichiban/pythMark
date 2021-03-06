from collections import defaultdict
import re
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

print(word_dict)