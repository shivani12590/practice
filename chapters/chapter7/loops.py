int = 1
while int < 10:
    print(int)
    int = int + 1

print("done")

i = 1
while i <= 10:
    print(i)
    i = i + 1

# print("done")
i = 10
while i >= 1:
    print(i)
    i = i - 1

i = 1
while i <= 10:
    print(i * 7)
    i = i + 1

j = 7
while j <= 70:
    print(j)
    j = j + 7

fruits = ["banana", "mango", "strawberry"]
a = len(fruits)
i = 0
while (i <= a - 1):
    print(fruits[i])
    i = i + 1

for item in fruits:
    print(item)

for i in range(10, 20, 3):
    print(i)
else:
    print("deone")

for i in range(0, 10):
    print(i)
    if i == 5:
        break

for i in range(15, 30):
    print(i)
    if i == 20:
        continue

li1 = [1, 2, 3]
for i in li1:
    pass

i = 19
if i > 18:
    print("pass")
else:
    print("failed")

if i > 19:
    print("eligible")
elif i > 18:
    print("ok")
else:
    print("invalid")

age = 18
vacc = 2
if age > 18:
    if vacc == 2:
        print("eligible")
    else:
        print("not eligible")
else:
    print("not eligible")



if age > 17 and vacc == 2:
    print("eligible")


i=0
while i<10:
    print("")
    i=i+1


for i in range(0,1):
 print(i)
