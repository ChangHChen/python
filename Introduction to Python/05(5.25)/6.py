f = open("article.txt", mode= "r", encoding="utf-8")
count = {}
art = ""
for line in f:
    art = art + " " + line
    words = art.split()
f.close()
print(words)
for word in words:
    if "," in word or "." in word:
        word = word[:len(word) - 1]
    if word not in count.keys():
        count[word] = 1
    else:
        count[word] += 1
for word in count.keys():
    print(f"{word}:{count[word]}")
