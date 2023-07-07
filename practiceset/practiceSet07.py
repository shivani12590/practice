# question 1

a = int(input("enter number"))
i = 1
while i <= 10:
    print(i * a)
    i = i + 1

for i in range(1, 11):
    print(str(a)+"X"+str(i)+"="+ str(i * a))


# question 2

li=["shivani","arbaz","sdika","aditya","aniket"]
for i in li:
    if i.startswith('s'):
     print(i)

# question 4

i=2
c=0
a=int(input("enter number"))
for i in range(2,a):
    if a/i == 0:
        c = c+1
print(c)
if c == 0:
    print("it is prime")
else:
    print("not prime")




