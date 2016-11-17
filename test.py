# Text file to string.
with open("C:/home/pythMark/texts/sherlock.txt") as f:
    text = f.read()
count = 0
for word in text.split():
    if word == "Sherlock":
        count += 1

print(count)


