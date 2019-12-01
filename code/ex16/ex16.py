from sys import argv

script, filename = argv

print(f"これから{filename}を消去する。")
print("消去したくないならCTRL-C (^C)を入力し、")
print("消去してもよいならEnterキーを入力する。")

input("?")

print("ではファイルを開こう...")
target = open(filename, 'w')

print("ファイルを切り捨てる。グッバイ!")
target.truncate()

print("3行分の内容を入力する。")

line1 = input("1行目: ")
line2 = input("2行目: ")
line3 = input("3行目: ")

print("これらをファイルに書き込む。")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("最後にファイルを閉じる。")
target.close()
