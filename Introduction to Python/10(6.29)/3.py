import re
import urllib.request

url = "https://www.ips.media.osaka-cu.ac.jp/?page_id=665l"
encoding = "utf-8"

with urllib.request.FancyURLopener().open(url) as fh:
    url_list = []
    for rawline in fh:
        line = rawline.decode(encoding).rstrip()
        match = re.search(r'<a href="(http[^"]+)">', line)
        if match:
            target = match.group(1)
            if target not in url_list:
                url_list.append(target)

for item in url_list:
    print(item)
