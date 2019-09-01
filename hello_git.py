
print("Hello, Github")##commenting
print("Good bye")

#Tack for att du raddade allt!


def main():
	to_print=''
	user_in = input("write something to see it change ")

	for i in user_in:
		if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
			to_print += i
		else:
			to_print += i + "o" + i
	print("result is here ", to_print)

main()  
