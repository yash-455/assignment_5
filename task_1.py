dictionary = {
    "Nick": "95",
    "John": "70",
    "Mike": "80",
    "Alice": "90",
    "Bob": "75"}

Name = str(input("Enter name of student: "))
if Name in dictionary:
    print(f"Marks of {Name} is: {dictionary[Name]}")
else:
    print(f"No student named {Name} found in the dictionary")