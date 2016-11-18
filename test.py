with open("C:/home/pythMark/texts/sherlock.txt") as f:
    text = f.read()
words = text.split()
word_set = set(words)
word_dic = dict.fromkeys(word, [])

for w in word_set:
    word_dic[w].append(1)

print(word_dic)