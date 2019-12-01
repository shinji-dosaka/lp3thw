def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"チーズが{cheese_count}個!")
    print(f"クラッカーが{boxes_of_crackers}箱!")
    print("パーティーには十分な量だ!")
    print("ブランケットをもって出かけよう。\n")


print("関数にそのまま数値を渡すことができる:")
cheese_and_crackers(20, 30)

print("スクリプトの変数を使うこともできる:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("計算結果を渡すこともできる:")
cheese_and_crackers(10 + 20, 5 + 6)

print("もちろん、変数と計算を組み合わせることもできる:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
