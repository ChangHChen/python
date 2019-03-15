import re
import urllib.request

url = "https://www.ips.media.osaka-cu.ac.jp/?page_id=180"
encoding = "utf-8"

with urllib.request.FancyURLopener().open(url) as fh:
    count_heading = 0
    for rawline in fh:
        line = rawline.decode(encoding).rstrip()
        match = re.search(r"(<h[1-6]>)", line)
        if match:
            count_heading += 1

print(url, "の内容に、見出しの数は", count_heading, "行ありました")