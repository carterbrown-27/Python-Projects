import random
import importlib

numgames = 100
wins = 0
gamesplayed = 0
guesses = 6
letters = []
wordlist = []
ai_module = None
init_round = None
make_guess = None


def initgame():
	global wordlist, gamesplayed, wins
	gamesplayed = 0
	wins = 0
	filein = open("base-words.txt", "r")
	wordlist = filein.read().split("\n")
	filein.close();

def gameround():
	global wins, gamesplayed

	word = random.choice(wordlist).lower()
	initword = ""
	for i in word:
		initword += "_"

	init_round(initword)
	guessed = []
	wrong = 0
	won = False
	while wrong < guesses:
		puzzle = ""
		argument = ""
		correct = 0
		for char in word:
			if char in guessed:
				puzzle += char + " "
				argument += char
				correct += 1
			else:
				argument += "_"
				puzzle += "_ "
		if correct >= len(word):
			won = True
			break
		print("Your guesses so far: " + str(guessed))
		print("Current Puzzle: " + puzzle)
		print("Remaining Incorrect Guesses:", (guesses - wrong))
		guess = make_guess(argument)
		if guess not in word:
			wrong += 1
		if guess not in guessed:
			guessed.append(guess)

	gamesplayed += 1
	if won:
		print("You won the round!")
		print("The word was "+word)
		wins += 1
	else:
		print("You lost the round. The word was " + word);


def main():
	global ai_module, init_round, make_guess
	try:
		ai_module = importlib.import_module("hangman-ai")
		init_round = getattr(ai_module, "initround")
		make_guess = getattr(ai_module, "makeguess")
	except Exception as err:
		print("Error loading module and/or functions - check the names?")
		print("Error message:")
		print(err)
		quit()

	initgame()
	for round in range(numgames):
		gameround()
	print("Games Played:", gamesplayed)
	print("Games Won:", wins)

if __name__ == "__main__":
	main()
