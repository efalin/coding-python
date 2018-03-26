import sys

def getCommand():
	command = input("Type a command: ")
	return command

def listOfCommands():
	print("Here is a list of commands you can use: Raise Shields, Fire Missiles, Contact Avengers, Contact SHIELD, Exit Program")

def raiseShields(): 
	print("The perimeter shields have been raised")

def fireMissiles():
	print("All Mark III missiles have been fired")

def exitProgram():
	print("Aborting the mission now")
	sys.exit(0)

def contactAvengers():
	print("The Avengers are being contacted. They will arrive in approximately four point three minutes")

def contactSHIELD():
	print("If you say so. SHIELD is being informed")


while True:
	command = getCommand()

	if command.lower() == "raise shields":
		raiseShields()
	elif command.lower() == "fire missiles":
		fireMissiles()
	elif command.lower() == "exit program":
		exitProgram()
	elif command.lower() == "contact avengers":
		contactAvengers()
	elif command.lower() == "contact shield":
		contactSHIELD()
	elif command.lower() == "options":
		listOfCommands()
	else:
		print("Not understood")