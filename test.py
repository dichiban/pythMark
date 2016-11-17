# Text file to string.
with open("C:/home/pythMark/texts/sherlock.txt") as f:
    text = f.read()
words = text.split()
word = set(words)
word_dic = dict.fromkeys(word, 0)


for w in word:
    word_dic[w] = words.count(w)

print(word_dic)
#word_dic = dict.fromkeys(set(words), 0)
#for word in words:
#    for word2 in word_dic:
#        if word2 == word:
#            word_dic[word2] += 1


        



