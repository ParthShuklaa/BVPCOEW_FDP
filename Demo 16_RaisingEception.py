Age = int(input("Enter your Age "))

if not type(Age) is int:
    raise TypeError ("Entered No is not integer")
    if Age <15:
        raise Exception("Minor Age Alert")

