import re
import urllib.request

url = "http://shakespeare.mit.edu/hamlet/hamlet.1.2.html"
encoding = "utf-8"


def count_input(dic, key):
    if key in dic.keys():
        dic[key] += 1
    else:
        dic[key] = 1


with urllib.request.FancyURLopener().open(url) as fh:
    count_hamlet_1_2 = {}
    for rawline in fh:
        line = rawline.decode(encoding).rstrip()
        match = re.search(r"<A NAME=[0-9]+>(.+)</A>", line)
        if match:
            sentence = match.group(1).lower()
            sentence = re.sub(r"[;:,.!?]", "", sentence)
            for word in sentence.split():
                for letter in word:
                    count_input(count_hamlet_1_2, letter)

for alphabet in "abcdefghijklmnopqrstuvwxyz":
    if alphabet in count_hamlet_1_2.keys():
        print(alphabet, "...", count_hamlet_1_2[alphabet])
