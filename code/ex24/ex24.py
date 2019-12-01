print("すべてのことを'練習'しよう。")
print('そのためには、\\を使った\'エスケープ\'を理解する必要がある。')
print('\nは改行で\tはタブだ。')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
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

# これは文字列をフォーマットする別の方法だ
print("この数で始めよう: {}".format(start_point))
# これはf""文字列を使った方法だ
print(f"豆が{beans}個、瓶が{jars}個、木箱が{crates}個。")

start_point = start_point / 10

print("このようにすることもできる。")
formula = secret_formula(start_point)
# これはフォーマット文字列にリストを適用する便利な方法だ
print("豆が{}個、瓶が{}個、木箱が{}個。".format(*formula))
