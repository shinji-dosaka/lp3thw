print("""君は二つの扉がある暗い部屋に入った。
扉1と扉2のどちらに進むか?""")

door = input("> ")

if door == "1":
    print("そこには、チーズケーキを食べている巨大なクマがいる。")
    print("どうする?")
    print("1. ケーキを奪う。")
    print("2. クマに向かって叫ぶ。")

    bear = input("> ")

    if bear == "1":
        print("クマは君の頭をかじった。なんてことだ!")
    elif bear == "2":
        print("クマは君の足をかじった。なんてことだ!")
    else:
        print(f"そう、おそらく{bear}が一番よいだろう。")
        print("クマは逃げた。")

elif door == "2":
    print("深い闇へと続くクトゥルフの目をのぞき込む。")
    print("何が見える?")
    print("1. ブルーベリー")
    print("2. 黄色いジャケット")
    print("3. メロディを奏でるリボルバー")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("なんとか生きているが自分を見失っている。")
        print("なんてことだ!")
    else:
        print("狂気によって目の前が汚物の海と化す。")
        print("なんてことだ!")

else:
    print("君はよろけてナイフの上に落ちて死んだ。なんてことだ!")
