# Text file to string.
with open("C:/home/pythMark/texts/sherlock.txt") as f:
    text = f.read()


print(len(text.split()))
print(len(set(text.split())))


