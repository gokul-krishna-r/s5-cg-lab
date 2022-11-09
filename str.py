a=raw_input('Enter String: ')
x=raw_input("Enter Character to Check Occurence: ")
print("The total count of occurence of "+x+" is ",a.count(x))
y=raw_input("Enter substring to find: ")

if (a.find(y)>0):
	print(a.find(y))
else:
	print("Character is not present")
print("Length of String is ",len(a))
z=raw_input("Enter string to append: ")
a=a+z
print(a)
