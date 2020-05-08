
name = input("Enter your Name !!")
age = int(input("Enter your age"))
no = int(input("Enter no you want to divide" ))
try:
    print(name)
    value = age/no

except ZeroDivisionError:
    print("You can't divide any no by zero")
else:
    print(value)
#except:
   # print("You can't Show undefined variable")
finally:
    print("Thank you using my Application!!!!")