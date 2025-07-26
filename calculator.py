print("\t SIMPLE CALCULATOR \n")
print("\n select your desired operation:\n1.addition\n2.subtraction\n3.multiplication\n4.division")
choice =input("enter your choice (1/2/3/4)")
num1=float(input("enter a number:"))
num2=float(input("enter a another number:"))
if choice =='1':
    result=num1+num2
    print("result:",result)
elif choice =='2':
    result=num1-num2
    print("result:",result)
elif choice =='3':
    result=num1*num2
    print("result:",result)
elif choice =='4':
    if num2!=0:
        result=num1/num2
        print("result:",result)
    else:
        print("error:division by zero is not possible")
else:
    print("invalid choice")

