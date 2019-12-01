from sys import argv

script, user_name = argv
prompt = '> '

print(f"やぁ、{user_name}。私は{script}スクリプトです。")
print("私は君にいくつかの質問をしたいと思います。")
print(f"{user_name}、君は私のことが好きですか?")
likes = input(prompt)

print(f"{user_name}、君はどこに住んでいますか?")
lives = input(prompt)

print("君はどんな種類のコンピュータをもっていますか?")
computer = input(prompt)

print(f"""
いいね。私のことが好きですかと聞いたら、君は「{likes}」といった。
君は{lives}に住んでいる。私にはどこかわからないけどね。
それに、君は{computer}コンピュータをもっている。すごいね。
""")
