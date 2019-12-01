import random
from urllib.request import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "%%%という名前のクラスを作成する。このクラスは%%%クラスを継承する。",
    "class %%%(object):\n    def __init__(self, ***):":
      "%%%クラスは__init__関数をもつ。この関数のパラメータはselfと***だ。",
    "class %%%(object):\n    def ***(self, @@@):":
      "%%%クラスは***関数をもつ。この関数のパラメータはselfと@@@だ。",
    "*** = %%%()":
      "***変数に%%%クラスのインスタンスを設定する。",
    "***.***(@@@)":
      "***の関数である***をselfと@@@を引数にして呼び出す。",
    "***.*** = '***'":
      "***の属性である***に'***'を設定する。"
}

# 慣用句を練習するかどうか?
if len(sys.argv) == 2 and sys.argv[1] == "japanese":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# ウェブサイトから単語を読み込む
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence

        # クラス名を置き換える
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # それ以外を置き換える
        for word in other_names:
            result = result.replace("***", word, 1)

        # パラメータリストを置き換える
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# CTRL-Dを入力するまで繰り返す(Windowsの場合はCTRL-Z)
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"{answer}\n\n")
except EOFError:
    print("\n終わり")
