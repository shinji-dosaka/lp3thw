cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("今日は", cars, "台の車が利用可能。")
print("今日は", drivers, "人しかドライバーがいない。")
print("だから", cars_not_driven, "台の車にはドライバーがいない。")
print("今日は", carpool_capacity, "人の乗客を運べる。")
print("今日は", passengers, "人の乗客がいる。")
print("一台の車に", average_passengers_per_car,
      "人を乗せる必要がある。")
