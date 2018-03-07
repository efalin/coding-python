from random import randint
goodanswer = False
password = randint(1, 100)
print("SECURE LOGIN SYSTEM")


while not goodanswer:
	answer = int( input("Enter Password: " ) )
if answer > password:
	print("Access Denied – Your entry was too high")
elif answer < password:
	answer < password print("Access Denied – Your entry was too low")

else:
	print("Access Granted")




