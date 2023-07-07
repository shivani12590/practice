# question 1

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))


def greatest(a1=12, b1=56, c1=45):
    if a1 > b1 and a1 > c1:
        print("maximum value is ", a1)
    elif b1 > a1 and b1 > c1:
        print("maximum value is", b1)
    elif c1 > a1 and c1 > b1:
        print("maximum value is", c1)
    else:
        print("invalid")


greatest(a,b,c)

greatest()

