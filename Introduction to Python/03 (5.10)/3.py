route = ["天王寺", "美章園", "南田辺", "鶴ヶ丘", "長居", "我孫子町", "杉本町"]
start = int(input("どこから："))
end = int(input("どこまで："))
while start >= end or start < 0 or end > 6:
    print("誤りがあり、改めて入力してくだいさい")
    start = int(input("どこから："))
    end = int(input("どこまで："))
for i in range(end+1 - start):        #終点も表示したいんだから、"+1"がなければ行かない
    print(i + start, route[i + start]) #i　は0から　1ずつ増加するから、”i + start"が求められる値になること