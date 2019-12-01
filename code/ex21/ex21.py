def add(a, b):
    print(f"加算 {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"減算 {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"乗算 {a} * {b}")
    return a * b

def divide(a, b):
    print(f"除算 {a} / {b}")
    return a / b


print("関数を使って計算をやってみよう!")

age = add(30, 9)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"年齢: {age}, 身長: {height}, 体重: {weight}, IQ: {iq}")


# 追加のパズル。とにかくこれを入力しよう。
print("パズルをやってみよう。")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("結果:", what, "手で計算したのと同じ結果になっただろうか?")
