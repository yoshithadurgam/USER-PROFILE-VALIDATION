name = "YOSHITHA"
name_length = len(name)
marks = [95, 84, 66, 45, 37]
valid_no = 0
fail_no = 0
for mark in marks:
    if mark < 0 or mark > 100:
        category = "Invalid"
    else:
        valid_no += 1
        if mark >= 90:
            category = "Excellent"
        elif mark >= 75:
            category = "Very Good"
        elif mark >= 60:
            category = "Good"
        elif mark >= 40:
            category = "Average"
        else:
            category = "Fail"
            fail_no += 1
        if name_length % 2 == 0 and mark >= 75:
            category = category + " (Top Performer)"
    print(mark, "-", category)
print("Total Valid Students:", valid_no)
print("Total Failed Students:", fail_no)
