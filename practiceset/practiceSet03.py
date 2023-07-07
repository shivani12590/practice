# question 1

name = input("enter your name")
print("good afternoon ,", name)

# question 2

name = input("enter name")
date = input("enter date")

letter = '''dear <!name>
you are selected!
<!date>'''
letter = letter.replace("<!name>", name)
letter = letter.replace("<!date>", date)
print(letter)

# question 3
string = "shivani anil  padale"
print(string.find("  "))

# question 4
print(string)
string = string.replace("  ", " ")
print(string)

# question 5
letter = "dear shivani,this course is good. thanks!"
print(letter)
formattedLetter = "dear shivani,\n\t\'this course is good.\'\nthanks"
print(formattedLetter)
