from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("まずファイル全体を出力する:")

print_all(current_file)

print("最初に巻き戻して、")

rewind(current_file)

print("先頭の3行を出力する:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
