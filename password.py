from random import randint
happened = False
password = randint(1, 100)
print("SECURE LOGIN SYSTEM")
answer = float( input("Enter Password: " ) )

if answer > password:

print("Access Denied – Your entry was too high")
answer = float( input("Enter Password: " ) )

if answer < password:
	print("Access Denied – Your entry was too low")
	answer = float( input("Enter Password: " ) )



