import re
import urllib.request

url = "http://shakespeare.mit.edu/hamlet/hamlet.1.5.html"
encoding = "utf-8"
proxy = {"http": "http://prxy.ex.media.osaka-cu.ac.jp:10080",
         "https": "http://prxy.ex.media.osaka-cu.ac.jp:10080"}

with urllib.request.FancyURLopener(proxy).open(url) as fh:
    words_after_the = []
    for raw_line in fh:
        line = raw_line.decode(encoding).rstrip()
        match = re.search(r"<A NAME=[0-9]+>(.+)</A>", line)
        if match:
            sentence = match.group(1).lower()
            sentence = re.sub(r"[,.?!;:]", "", sentence)
            sentence = sentence.split()
            for i in range(len(sentence)):
                if sentence[i] == "the":
                    word = sentence[i+1]
                    word = re.sub(r"[^a-z]+$", "", word)
                    words_after_the.append(word)

print(f"all words appeared after the word 'the':")
for item in words_after_the:
    print(item)