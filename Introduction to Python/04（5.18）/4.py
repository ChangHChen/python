count = {}
article = ""
line = str(input("Enter some sentences(END for terminate):"))
while True:
    if line == "END":
        break
    article = article + " " + line
    line = str(input())

words = article.split()
print(words)
for word in words:
    if "," in word or "." in word:
        word = word[:len(word) - 1]
    if word not in count.keys():
        count[word] = 1
    else:
        count[word] += 1

for word in count.keys():
    print(word, ":", count[word])

