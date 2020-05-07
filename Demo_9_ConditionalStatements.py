'''My_Age = int(input("Enter your Age\n"))
#input() is used for taking input
#Ways for implementing Conditional Loop
if My_Age>18:
    print("You can Vote")
else:
    #print("You can't Vote, Watch Cartoon Network")
    pass

#Short hand ways of writing Statement
if My_Age>18 :print("You can Watch Action movies ")

print("you can Eat sweets After dinner") if My_Age>18 else print("Eat sweet and brush your teeth")
'''

i = 0
while i<=10:

    print(i)
    if i == 4:
        continue
    i += 1