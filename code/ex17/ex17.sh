# echoの結果をリダイレクト(>)してサンプルファイルを作る。
echo "これはテストファイルです。" > test.txt

# 次にファイルの中身をcatで確認する。
cat test.txt

# ではこのファイルを使ってスクリプトを実行する。
python3 ex17.py test.txt new_file.txt
