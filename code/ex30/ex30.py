people = 30
cars = 40
trucks = 15

if cars > people:
    print("車に乗ろう。")
elif cars < people:
    print("車に乗らない方がよさそうだ。")
else:
    print("車に乗るかどうか決められない。")

if trucks > cars:
    print("トラックがたくさんある。")
elif trucks < cars:
    print("トラックに乗った方がよいかも。")
else:
    print("車とトラックのどちらにすべきか決められない。")

if people > trucks:
    print("よし、トラックに乗ろう。")
else:
    print("わかった。外出は控えよう。")
