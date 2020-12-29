from sys import argv
s,fr,fw= argv
print(f"We will read from {fr} and write in {fw}.")
file1=open(fr,'r')
file2=open(fw,'w')
file2.write(file1.read())
file2.close()
file2=open(fw,'r')
print(file2.read())
