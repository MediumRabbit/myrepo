string = "hello"
print(string.find("l"))  #finds indice of first 'e' in 'hello'
print(string.find("z"))  #if it's not found, python returns -1

string2 = "bdsbdsuibbckbviuvcdjcbdv"
print(string2.count("b"))  #count() counts how many times the argument appears
print(string2.count("3"))


print("\n"+"="*30)
print("""Requirements:
- Must not contain dashes(-)
- Must contain at least three a's""")

validPassword = False
while validPassword == False:
	password = input("\nEnter a password: ")
	if password.find("-") != -1:
		print("No dashes!")
	elif password.count("a") < 3:
		print("Must contain 3 or more a's")
	else:
		print("Good password!")
		validPassword = True
print("="*30)
