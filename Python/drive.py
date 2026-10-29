name=input("Enter your name: ")
age=int(input("Enter your age:"))
if(age>=18):
    if(age>=80):
        print(f"sorry {name} You cannot drive")
    else:
        print(f"hello {name} can drive")
else:
    print(f"sorry {name} can not drive")