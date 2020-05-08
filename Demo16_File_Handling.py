#Step1: Opening a file
#Step3: Read/Write a file
#Step4: Closing file

Myfile =  open("MyDetails.txt",'r')
Output = Myfile.readlines()
print(Output)
Myfile.close()

Myfile = open("MyDetails.txt",'a')
changes = input("Enter the changes you want in your file....")
Myfile.writelines(changes)
print("****************************************************")
Myfile =  open("MyDetails.txt",'r')
Output = Myfile.readlines()
print(Output)
Myfile.close()


