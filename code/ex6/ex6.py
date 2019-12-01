types_of_people = 10
x = f"世の中には{types_of_people}種類の人間がいる。"

binary = "バイナリ"
do_not = "そうでない"
y = f"{binary}を知っている人と、{do_not}人だ。"

print(x)
print(y)

print(f"私はいった: {x}")
print(f'こうともいった: "{y}"')

hilarious = False
joke_evaluation = "このジョークは面白かったかな?! {}"

print(joke_evaluation.format(hilarious))

w = "これは左側のテキストで..."
e = "これは右側のテキストだ。"

print(w + e)
