import random

## JS's First Python Code:
## Validates users input for integer and punishes the player
#def checkForCheater(usersInput):
#	if usersInput is not int:
#		print("Srsly? For real?")
#		randomSpanks = len(usersInput)
#		exit(str(randomSpanks) + " spanks, the programmer chooses the tool ]:->")

def checkForCheater(usersInput):
	if usersInput is not int:
		print("Come on! We've talked about numbers, haven't we?")
		randomSpanks = len(usersInput)
		exit("All you deserve is " + str(randomSpanks) + " spanks and your partner chooses the tool.")

def getSexStuff(numberOfActivities, selection):

	sexStuff = ["vaginal sex", "oral sex", "anal sex", "hand job", "strap-on", "no sex", "double penetration", "double dildo", "fisting", "deep throat", "foot job", "boob job"]
	funStuff = ["cane", "whip", "paddle", "nipple clamps", "cock ring", "blindfolds", "wax", "hooks", "butt plug", "biting", "slapping", "spanking", "hair pulling", "ice", "scratching", "teasing", "hairbrush spanking"]
	restraintStuff = ["gag", "cuffs", "bondage harness", "arms bondage", "legs bondage", "stockings bondage", "spreader bar", "dungeon irons", "straight jacket", "collar", "locked in", "chastity belt", "eye contact restriction", "orgasm denial"]
	playStuff = ["age play", "pet play", "breath play", "D/s play", "slave play", "rope play", "role play"]

	if selection == "sexStuff":
		selectedList = sexStuff
	elif selection == "funStuff":
		selectedList = funStuff
	elif selection == "restraintStuff":
		selectedList = restraintStuff
	elif selection == "playStuff":
		selectedList = playStuff

	if numberOfActivities < 1:
		print("Come on, pick at least one.")
		return ""
	elif numberOfActivities > len(selectedList):
		print("Sorry, that's too much fun even for you. Try again with number " + str(len(selectedList)) + " or lower.")
		return ""
	sexFun = random.SystemRandom()
	haveSexFun = sexFun.sample(selectedList, numberOfActivities)
	return haveSexFun

print("Hello stranger! How about spicing your sex life up a bit? We did all the hard work for you so all that's up to you is to choose some numbers. Let's play!")

result = ""
while result == "":
	inputSex = input("It's pretty easy for a start: How many sex activities would you like to experience? ")
	checkForCheater(inputSex)
	result = getSexStuff(int(inputSex), "sexStuff")
print("Nice! You're definitely going to enjoy " + str(result))

result = ""
while result == "":
	inputFun = input("Ouch! These are going to be so much fun! Tell me, how much? ")
	checkForCheater(inputFun)
	result = getSexStuff(int(inputFun), "funStuff")
print("No pain, no gain! " + str(result))

result = ""
while result == "":
	inputRest = input("There's nothing we would deny you. Or isn't there? Pick a number, you little bitch! ")
	checkForCheater(inputRest)
	result = getSexStuff(int(inputRest), "restraintStuff")
print("Oh-la-la. It's just the things you like! " + str(result))

result = ""
while result == "":
	inputPlay = input("Would you like to play? Of course you would. Tell us, what number is on your mind? ")
	checkForCheater(inputPlay)
	result = getSexStuff(int(inputPlay), "playStuff")
print("Well, look at that! " + str(result))

print("Be safe & have fun! ❤")