from sys import exit


def gold_room():
    print("この部屋は金塊でいっぱいだ。金塊をいくつ取る?")

    choice = input("> ")

    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("数字を入力する方法を学ぼう。")

    if how_much < 50:
        print("素晴らしい。君は欲深くない。君の勝ちだ!")
        exit(0)
    else:
        dead("君は強欲なろくでなしだ!")


def bear_room():
    print("この部屋にはクマがいる。")
    print("クマはたくさんのはちみつをもっている。")
    print("その太ったクマは隣の部屋の扉の前に居座っている。")
    print("どうやってそのクマをどかそう?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "はちみつを奪う":
            dead("クマは君を見て、そして、君は顔を殴られた。")
        elif choice == "クマをおどかす" and not bear_moved:
            print("クマは扉の前から移動した。")
            print("いまなら扉を通ることができる。")
            bear_moved = True
        elif choice == "クマをおどかす" and bear_moved:
            dead("君はクマを怒らせて、足をかじられた。")
        elif choice == "扉を開ける" and bear_moved:
            gold_room()
        else:
            print("君が何をいっているのかわからない。")


def cthulhu_room():
    print("この部屋には邪悪なクトゥルフがいる。")
    print("そいつに見つめられて、君は気がおかしくなる。")
    print("君は命懸けで逃げるか、自分の頭をかじるか?")

    choice = input("> ")

    if "逃げる" in choice:
        start()
    elif "頭" in choice:
        dead("おいしかった!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "なんてことだ!")
    exit(0)


def start():
    print("君は暗い部屋にいる。")
    print("右と左に扉がある。")
    print("どちらの扉を開ける?")

    choice = input("> ")

    if choice == "左":
        bear_room()
    elif choice == "右":
        cthulhu_room()
    else:
        dead("君は部屋のあちこちでつまずき、そして、餓死した。")


start()
