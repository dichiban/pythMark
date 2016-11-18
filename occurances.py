from collections import defaultdict
import re
# Text file to string.
with open("C:/home/pythMark/texts/sherlock.txt") as f:
    text = f.read().lower()

text = re.sub('[^a-z\ \']+', " ", text)
words = list(text.split())
word = set(words)
word_dict = defaultdict(list)

for w in words:
    word_dict[w].append(w)

print(word_dict)