formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("一", "二", "三", "四"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "好きな文を",
    "ここに書いてみよう",
    "たとえば詩や",
    "歌なんかもよいだろう"
))
