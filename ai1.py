import sys

def getCommand():
	command = input("Type a command: ")
	return command

def listOfCommands():
	print("Here is a list of commands you can use: Raise Shields, Fire Missiles, Exit Program")

def raiseShields(): 
	print("The perimeter shields have been raised")

def fireMissiles():
	print("All Mark III missiles have been fired")

def exitProgram():
	print("Aborting the mission now")
	sys.exit(0)


while True:
	command = getCommand()

	if command.lower() == "raise shields":
		raiseShields()
	elif command.lower() == "fire missiles":
		fireMissiles()
	elif command.lower() == "exit program":
		exitProgram()
	else:
		print("Not understood")