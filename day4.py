raw = input("Enter elements separated by space: ")
parts = raw.split(" ")
data = []
for value in parts:
    if value == "":
        continue
    is_num = True
    for ch in value:
        if ch < '0' or ch > '9':
            is_num = False
    if is_num == True:
        data.append(int(value))
    else:
        data.append(value)
num_box = []
str_box = []
num_cnt = 0
str_cnt = 0
for element in data:
    if element == "":
        continue
    if type(element) == int:
        num_box.append(element)
        num_cnt = num_cnt + 1
    elif type(element) == str:
        str_box.append(element)
        str_cnt = str_cnt + 1
print("this is my personalized code")
last_digit = 7
if last_digit % 2 == 0:
    flip_nums = []
    index = num_cnt - 1
    while index >= 0:
        flip_nums.append(num_box[index])
        index = index - 1
    num_box = flip_nums
else:
    flip_strs = []
    index = str_cnt - 1
    while index >= 0:
        flip_strs.append(str_box[index])
        index = index - 1
    str_box = flip_strs
print("Numbers List:", num_box)
print("Strings List:", str_box)
print("number count:", num_cnt)
print("string count:", str_cnt)
print("Numbers found =", num_cnt)
print("Strings found =", str_cnt)
