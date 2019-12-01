from sys import argv

script, filename = argv

txt = open(filename)

print(f"{filename}の内容は次のとおり:")
print(txt.read())

print("もう一度ファイル名を入力しよう:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
