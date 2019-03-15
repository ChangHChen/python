import re
import urllib.request

url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html"
encoding = "utf-8"

all_contents = []
with urllib.request.FancyURLopener().open(url) as fh:
    for raw_line in fh:
        line = raw_line.decode(encoding)
        all_contents.append(line)

for item in all_contents:
    match = re.search(r"<body", item)
    match2 = re.search(r'(id="yjw_week")', item)
    if match:
        num_body = all_contents.index(item)
    elif match2:
        num_id = all_contents.index(item)

for i in range(num_id, len(all_contents)):
    match3 = re.search(r"</table>", all_contents[i])
    if match3:
        num_table = i
        break


f = open("週間天気予報.html", mode="a", encoding="utf-8")
for i in range(num_body):
    f.write(all_contents[i])

for i in range(num_id, num_table + 1):
    f.write(all_contents[i])

for item in all_contents:
    if "</body>" in item:
        f.write(item)

for item in all_contents:
    if "</html>" in item:
        f.write(item)
f.close()
