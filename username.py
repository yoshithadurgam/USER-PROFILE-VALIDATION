full_name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")
age = int(input("Enter Age: "))
is_valid = True
if full_name.startswith(" ") or full_name.endswith(" ") or full_name.count(" ") < 1:
    is_valid = False
if email.count("@") != 1 or email.count(".") < 1 or email.startswith("@"):
    is_valid = False
if len(mobile) != 10 or not mobile.isdigit() or mobile.startswith("0"):
    is_valid = False
if age < 18 or age > 60:
    is_valid = False
if is_valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
