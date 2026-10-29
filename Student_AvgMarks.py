m1 = float(input("Enter the Marks for the subject1: "))
m2 = float(input("Enter the Marks for the subject2: "))
m3 = float(input("Enter the Marks for the subject3: "))
avg = (m1+m3+m3)/3
print(f"Average of the marks is {avg}")
if avg >= 30:
    print("Result: Pass")
else:
    print("Result: Fail")