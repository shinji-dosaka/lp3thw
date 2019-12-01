the_count = [1, 2, 3, 4, 5]
fruits = ['りんご', 'オレンジ', '梨', 'あんず']
change = [1, 'ペニー', 2, 'ダイム', 3, 'クォーター']

# このforループはリストの要素を順にたどる。
for number in the_count:
    print(f"数: {number}")

# 上に同じ。
for fruit in fruits:
    print(f"果物: {fruit}")

# 混在した要素のリストも可能。
for i in change:
    print(f"小銭: {i}")

# リストを組み立てることもできる。まず空のリストから始める。
elements = []

# 次にrange関数を使って0から5まで数える。
for i in range(0, 6):
    print(f"リストに{i}を追加")
    # append関数はリストの関数だ。
    elements.append(i)

# ここでリストの内容を出力する。
for i in elements:
    print(f"リストの要素: {i}")
