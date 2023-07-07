# a=10
# print("hello")
# b=input("enter your name")
# c=int(input("enter no"))
#
# print(type(c),c)
# d=input("enter no")
# d=int(d)
# print(type(d),d)
#
# c='shivani'
# c='''shivani '''
# c="shivani"
# print(c[4:3])
#
# print(c.find('s'))
# print(c.capitalize())
# print(c.count('s'))
# print(c.endswith('ni'))
# print(c.replace("a","b"))
# print(c.index('a'))
#
#
#
# li=[1,2,3]
# lo1=["shivani","djs,",45,67.5]
# li3=[1,4,2,5,3]
# li3[0]=3
#
# li.sort()
# print(li)
#
# li.remove(2)
# print(li)
# li.pop(0)
# print(li)
# li.append(1)
# print(li)
#
# li.insert(0,23)
# print(li)
# li.reverse()
# print(li)
# li4=[]
# li4=li.copy()
# print(li4)
#
# tu=(10,2,3)
# print(tu.count(2))
# print(tu.index(10))
#
# tu1=()
# tu2=(19,)
# print(tu2)
# print(tu[0])
#
#
#
#
# D={}


n = 4
m = 1
for i in range(1, n + 1):
    m = m * i

print(m)


def recursive_function(n):
    if n == 0:
        return 0
    return n + recursive_function(n - 1)


print(recursive_function(4))

