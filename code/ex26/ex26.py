# ex11.py
print("君の年齢は?", end=' ')
age = input()
print("君の身長は?", end=' ')
height = input()
print("君の体重は?", end=' ')
weight = input()

print(f"そう、君は{age}歳で、身長は{height}で、体重は{weight}だ。")

# ex15.py
from sys import argv

script, filename = argv

txt = open(filename)

print(f"{filename}の内容は次の通り:")
print(txt.read())

print("もう1度ファイル名を入力しよう:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


# ex24.py
print("すべてのことを'練習'しよう。")
print('そのためには、\\を使った\'エスケープ\'を理解する必要がある。')
print('\nは改行で\tはタブだ。')

poem = """
\tすばらしい世界
論理がしっかりと根付いている
そこでは、愛の必要性を\n見つけることも
あふれ出る情熱を理解することもできない
説明が必要だ
\n\t\tそこにはなにもないことを
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"これは5になるべき: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# これは、文字列をフォーマットする別の方法だ
print("この数で始めよう: {}".format(start_point))
# これは、f""文字列を使った方法だ
print(f"豆が{beans}個、瓶が{jars}個、木箱が{crates}個。")

start_point = start_point / 10

print("このようにすることもできる。")
formula = secret_formula(start_point)
# これは、フォーマット文字列にリストを適用する便利な方法だ
print("豆が{}個、瓶が{}個、木箱が{}個。".format(*formula))


# ex29.py
people = 20
cats = 30
dogs = 15


if people < cats:
    print("猫が多すぎる! この世の終わりだ!")

if people > cats:
    print("あまり猫はいない! 世界は救われた!")

if people < dogs:
    print("世界はよだれまみれだ!")

if people > dogs:
    print("世界は乾いている!")


dogs += 5

if people >= dogs:
    print("人間は犬と同じかそれ以上だ。")

if people <= dogs:
    print("人間は犬と同じかそれ以下だ。")


if people == dogs:
    print("人間と犬は同じだ。")
