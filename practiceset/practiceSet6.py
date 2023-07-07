# question 1

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
d=int(input("enter 4th number"))
if(a>b and a>c and a>d):
    print("greatest number is ",a)
elif(b>a and b>c and b>d):
    print("greatest number is",b)
elif(c>a and c>b and c>d):
    print("greatest number is:",c)
elif(d>a and d>b and d>c):
    print("greatest number is :",d)
else:
    print("invalid numbers")