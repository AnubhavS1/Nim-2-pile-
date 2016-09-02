import random

numBerriesPile1 = 0
numBerriesPile2 = 0

def displayIntro():
	print('Welcome the the simple game of Nim.')
	print('In this game there are 2 piles of berries.')
	print('You can eat berries from one of these two piles.')
	print('If you eat the last berry then you lose.')

# randomize the number of berries in the piles
def randomNumBerries():
	numBerriesPile1 = random.randint(1, 100)
	numBerriesPile2 = random.ranint(1, 100)
	print('There are ' + str(numBerriesPile1) + ' berries in pile 1, and ' + str(numBerriesPile2) + ' berries in pile 2.')

def letPlayerGo():
	playerPileChoice = 0
	playerBerriesEaten = 0

	# Allow the user to input which pile they want to eat from
	while playerPileChoice == 0:
		print('What pile do you want to eat from?(1 or 2)')
		playerPileChoice = int(input())

		# Allow the user to input how many berries they want to eat if they picked pile 1
		if playerPileChoice == 1:
	 		print('How many berries do you want to eat from this pile?')
			playerBerriesEaten = int(input())
			numBerriesPile1 = numBerriesPile1 - playerBerriesEaten
			print('There are (' + numBerriesPile1 + ', ' + numBerriesPile2 + ') berries left.')

		elif playerPileChoice == 2:
			print('How many berries do you want to eat from this pile?')
			playerBerriesEaten = int(input())
			numBerriesPile2 = numBerriesPile2 - playerBerriesEaten
			print('There are (' + numBerriesPile1 + ', ' + numBerriesPile2 + ') berries left.')

		else:
			print('That is not a valid answer.')

def letComputerGo():
	# program computer AI so that it will always win
	computerBerriesEaten = 0
	computerPileChoice = 0
	while computerPileChoice == 0:
		if numBerriesPile1 > numBerriesPile2:
			computerPileChoice = 1
			


def gameFunction():
	print('Do you want to go first or second? (1 or 2)')
	firstOrSecond = int(input())
	if firstOrSecond == 1:
		print('You are going first!')
		letPlayerGo()
	else:
		print('You are going second!')
		letComputerGo()
