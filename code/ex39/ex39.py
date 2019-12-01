# 州と略称とのマッピングを作成する
states = {
    'オレゴン': 'OR',
    'フロリダ': 'FL',
    'カリフォルニア': 'CA',
    'ニューヨーク': 'NY',
    'ミシガン': 'MI'
}

# 州とその州の都市との基本セットを作成する
cities = {
    'CA': 'サンフランシスコ',
    'MI': 'デトロイト',
    'FL': 'ジャクソンビル'
}

# いくつかの都市を追加する
cities['NY'] = 'ニューヨーク'
cities['OR'] = 'ポートランド'

# いくつかの都市を出力する
print('-' * 10)
print("NY州の都市:", cities['NY'])
print("OR州の都市:", cities['OR'])

# いくつかの州を出力する
print('-' * 10)
print("ミシガン州の略称:", states['ミシガン'])
print("フロリダ州の略称:", states['フロリダ'])

# states辞書の値を取得し、それをcities辞書で使う
print('-' * 10)
print("ミシガン州の都市:", cities[states['ミシガン']])
print("フロリダ州の都市:", cities[states['フロリダ']])

# すべての州の略称を出力する
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state}州の略称は{abbrev}")

# 州の都市を出力する
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev}州の都市は{city}")

# これらを同時にやってみる
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state}州の略称は{abbrev}")
    print(f"そして、その州の都市は{cities[abbrev]}")

print('-' * 10)
# 存在しないかもしれない州の略称を安全に取得する
state = states.get('テキサス')

if not state:
    print("残念だが、テキサスは登録されていない。")

# デフォルト値を使って都市を取得する
city = cities.get('TX', '未登録')
print(f"'TX'州の都市: {city}")
