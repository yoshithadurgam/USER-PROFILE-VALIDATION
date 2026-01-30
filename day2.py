sid = input()
email = input()
pwd = input()
ref = input()
flag = True
if len(sid) != 7:
    flag = False
elif sid[0:3] != "CSE":
    flag = False
elif sid[3] != "-":
    flag = False
elif not (sid[4].isdigit() and sid[5].isdigit() and sid[6].isdigit()):
    flag = False
if flag:
    if "@" not in email or "." not in email:
        flag = False
    elif email[0] == "@" or email[-1] == "@":
        flag = False
    elif email[-4:] != ".edu":
        flag = False
if flag:
    if len(pwd) < 8:
        flag = False
    elif not pwd[0].isupper():
        flag = False
    elif not (
        pwd[0].isdigit() or pwd[1].isdigit() or pwd[2].isdigit() or
        pwd[3].isdigit() or pwd[4].isdigit() or pwd[5].isdigit() or
        pwd[6].isdigit() or pwd[7].isdigit()
    ):
        flag = False
if flag:
    if len(ref) != 6:
        flag = False
    elif ref[0:3] != "REF":
        flag = False
    elif not (ref[3].isdigit() and ref[4].isdigit()):
        flag = False
    elif ref[5] != "@":
        flag = False
if flag:
    print("APPROVED")
else:
    print("REJECTED")
