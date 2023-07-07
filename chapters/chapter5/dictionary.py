# creating dictionary

a = {
    1: "shivani",
    2: None,
    None: None

}
print(a)

# duplicate keys

a = {
    1: "shivani",
    2: "arbaz",
    2: "adika"

}
print(a)

# duplicate values

a = {
    1: "shivani",
    2: "adika",
    3: "adika"

}
print(a)

#can use any data type for key and value
d = {
    "1":"shivani",
    4:3,
    2.0:"shiv"
}
print(d)
print(d["1"])
print(d[4])

g = {
    "1":"shivani",
    4:3,
    2.0:"shiv"
}
print(g)
g["1"]="arbaz"
print(g)

# iterating keys
print(list(g.keys()))

# iterating values
print(list(g.values()))

#items
print(g.items())

di={
    "2":"adika"
}
g.update(di)
print(g)
g["3"]="aditya"
print(g)


print(di.get("1"))
