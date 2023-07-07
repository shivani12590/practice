# li=[]
# print(type(li))
# li=[1,2,34]
# print(li)
#
#
# t=(1,2,34)
#
# print(type(t))
# print(t)
#
# d={"1":"shivani"}
# print(type(d))
# print(d)
#
# set=set()
# set.add(1)
# print(set)
# print(type(set))

# create set

s={1,2,3}
print(s)

# empty set
s=set()
print(type(s))

# adding values
s.add(1)
s.add(23)
s.add((1,2,3))
print(s)

s.remove(23)
print(s)
len(s)

s.clear()
print(s)

a={3,4,5,7,89}
b={2,3,4,1}
c=set()
c=a.union(a,b)
print(c)

c=a.intersection(a,b)
print(c)

