# この関数はargvをもつスクリプトに似ている。
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# 確かに*argsではわかりにくい。こんな風に書くこともできる。
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# この関数は引数を一つだけ取る。
def print_one(arg1):
    print(f"arg1: {arg1}")

# この関数は引数を取らない。
def print_none():
    print("引数なし")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
