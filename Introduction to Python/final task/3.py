import re
import urllib.request

url = "http://shakespeare.mit.edu/hamlet/hamlet.1.4.html"
encoding = "utf-8"

proxy = {"http": "http://prxy.ex.media.osaka-cu.ac.jp:10080",
         "https": "http://prxy.ex.media.osaka-cu.ac.jp:10080"}

counting = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    counting[letter] = 0

with urllib.request.FancyURLopener(proxy).open(url) as fh:
    for raw_line in fh:
        line = raw_line.decode(encoding).rstrip()
        match = re.search(r"<A NAME=[0-9]+>(.+)</A>", line)
        if match:
            sentence = match.group(1).lower()
            sentence = re.sub(r"[,.?!;:]", "", sentence)
            for word in sentence.split():
                first_letter = word[0]
                last_letter = word[len(word)-1]
                if len(word) == 1:
                    counting[word] += 1
                elif first_letter == last_letter:
                    counting[first_letter] += 1

print("最初と最後の文字が同じ単語について，最初の文字(a, b, c, ...)毎に個数は：")
for letter in alphabet:
    if counting[letter] != 0:
        print(letter, ":", counting[letter])
