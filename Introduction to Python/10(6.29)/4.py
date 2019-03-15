import re
import urllib.request

url = "http://shakespeare.mit.edu/hamlet/hamlet.1.3.html"
encoding = "utf-8"


def count_word(dic, key):
    if key in dic.keys():
        dic[key] += 1
    else:
        dic[key] = 1


with urllib.request.FancyURLopener().open(url) as fh:
    all_word = {}
    all_word_count = {}
    count_line = 0
    for raw_line in fh:
        line = raw_line.decode(encoding).rstrip()
        match = re.search(r"<A NAME=[0-9]+>(.+)</A>", line)
        if match:
            count_line += 1
            sentence = match.group(1).lower()
            sentence = re.sub(r"[,.;:!?]", "", sentence)
            for word in sentence.split():
                all_word[word] = int(len(word))
                count_word(all_word_count, word)

longest_word = ["a"]
total_words = 0
total_letters = 0
for item in all_word.keys():
    if all_word[item] > int(len(longest_word[0])):
        longest_word.clear()
        longest_word.append(item)
    elif all_word[item] == int(len(longest_word[0])) and item != longest_word[0]:
        longest_word.append(item)

    total_words += all_word_count[item]
    total_letters += (all_word[item] * all_word_count[item])

avg = total_letters / total_words
count_the = all_word_count["the"]

print(f"最も長い単語は：{longest_word}である\n"
      f"一単語当たりの平均の文字数は：{avg:.2f}である\n"
      f"定冠詞'the'は{count_the}回出現している")
