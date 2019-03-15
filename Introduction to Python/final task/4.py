import re
import urllib.request

url = "http://rss.asahi.com/rss/asahi/newsheadlines.rdf"
encoding = "utf-8"

proxy = {"http": "http://prxy.ex.media.osaka-cu.ac.jp:10080",
         "https": "http://prxy.ex.media.osaka-cu.ac.jp:10080"}

with urllib.request.FancyURLopener(proxy).open(url) as fh:
    content = []
    for raw_line in fh:
        line = raw_line.decode(encoding)
        match = re.search(r"<title>(.+)</title>", line)
        if match:
            sentence = match.group(1)
            if not re.search(r"^<!\[CDATA\[", sentence):
                content.append(sentence)

for i in range(len(content)):
    print(content[i])
