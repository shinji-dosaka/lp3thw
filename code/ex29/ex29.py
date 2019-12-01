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
