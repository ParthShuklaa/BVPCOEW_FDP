MySet = {"Maths", "Stats","Computer","Electronics"}
print(MySet)

def Display():
    for element in MySet:
        print(element)
#Printing Elements one by one
Display()
MySet.add("Pysics")
print("...........................")

MySet.pop()
#MySet.update("Maths")

Display()
print("...........................")
MySet.add("Chemistry")
MySet.add("Maths")
MySet.add("Applied Algo")
MySet.add("Applied Physics")

Display()
MySet.add("Applied Algo")
MySet.add("Applied Physics")

print("...........................")

Display()
