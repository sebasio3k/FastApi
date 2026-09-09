# and
age = 29
licensed = True

if age >= 18 and licensed:
    print("You can drive")
else:
    print("You can't drive")
    
# or
is_student = True
membership = False

if is_student or membership:
    print("You have a discount")
else:
    print("You don't have a discount")
    
# not
is_admin = False

if not is_admin:
    print("You are not an admin")
else:
    print("You are an admin")
    
# short circuit
# name = "Bastian"
name = False

print(name and name.upper())