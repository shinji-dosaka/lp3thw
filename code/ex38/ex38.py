ten_things = "りんご みかん カラス 電話 ライト 砂糖"

print("ちょっと待て。リストには要素が10個ない。それを修正しよう。")

stuff = ten_things.split(' ')
more_stuff = ["昼", "夜", "歌", "フリスビー",
              "トウモロコシ", "バナナ", "ガール", "ボーイ"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("追加:", next_one)
    stuff.append(next_one)
    print(f"現在、要素は{len(stuff)}個。")

print("このとおり:", stuff)

print("stuffに対していろいろとやってみよう。")

print(stuff[1])
print(stuff[-1])  # ワォ! すごくない?
print(stuff.pop())
print(' '.join(stuff))  # なんてクールだ!
print('#'.join(stuff[3:5]))  # 素晴らしい!
