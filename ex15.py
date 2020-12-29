from sys import argv
script , filename = argv
file = open(filename)
print(f"Here's your file {filename}:")
print(file.read())
print("Type the file name again:")
file2 = input("> ")
text = open(file2)
print(text.read())
