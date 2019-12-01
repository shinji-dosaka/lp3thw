from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"{from_file}から{to_file}へコピーする。")

# 次の2行を1行で書くことができる。どうすればよいだろうか?
in_file = open(from_file, 'rb')
in_data = in_file.read()

print(f"入力ファイルの大きさは{len(in_data)}バイト。")

print(f"出力ファイルは存在するか? {exists(to_file)}")
print("準備できた。続行するにはEnterキーを、中断するにはCTRL-Cを入力する。")
input()

out_file = open(to_file, 'wb')
out_file.write(in_data)

print("すべて完了した。")

out_file.close()
in_file.close()
