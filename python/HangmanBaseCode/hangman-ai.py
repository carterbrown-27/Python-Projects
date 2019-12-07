''' wrote this AI that wins games of hangman at around 95% success rate, n=1000. (words sampled from base-words.txt) '''

#add any global variables your AI needs here:
# $workingWordList = words possible for a given puzzle
workingWordList = []
guessedLetters = []

#wordlist is all possible words the game could pick as a puzzle
#it is only initialized when your module is imported, so do not change it
wordlist = []

#letters is a list of all characters your program could guess
#it is re-initialized each round, so you can modify it
letters = []
filein = open("base-words.txt", "r")
wordlist = filein.read().lower().split("\n")
filein.close();

#round initialization
#this is called at the start of each round
#the input string is a single _ for each character in the puzzle
def initround(string):
	#initializes the list of letters that could be guessed
	#you can use this list in your AI implementation if desired
	letters.clear()
	for i in range(ord('a'), ord('z')+1):
		letters.append(chr(i))

	#add any more initialization code your AI requires here
	#...
	global workingWordList
	workingWordList = wordlist.copy()
	guessedLetters.clear()

#Add your AI code to guess a letter here
#The input string is the current puzzle, with _ for any unguessed letters
#You should output one lower-case character
def makeguess(string):
	# trim down the workingWordList
	global workingWordList
	workingWordList = getPossible(string, workingWordList)
	# DEBUG: print("done")
	# pick letter given this smaller wordList.
	guess = pickLetter(workingWordList)
	guessedLetters.append(guess)
	return guess

# from a larger set of possible words, narrow it down given the current puzzle string
def getPossible(string, words):
	# DEBUG: print("screening words..." + string)
	# $possible = new list storing all elements from $words that match puzzle requirements
	possible = []
	for word in words:
		# must be same length (after first func call, does nothing)
		if len(word) != len(string): continue
		# checks compatibility
		for i in range(0,len(word)):
			# if character at i unknown
			if string[i] == "_":
				# exclude $word if the letter at this same position in $word has already been guessed
				# (if this word was correct, the letter guessed wouldn't still be unkown in the puzzle)
				if word[i] in guessedLetters:
					break
				# otherwise it can be any character
				else:
					continue
			# if there is an known letter, make sure $word has the same letter at this position
			if string[i] != word[i]: break
		# if the for loop ended without interruption, this word is still possible
		else:
			possible.append(word)
	return possible

def pickLetter(possible):
	# DEBUG: print("picking letter..." + str(len(possible)))
	letterFreqs = {}
	max = 0
	maxLetter = "?"
	# for every word that could be the solution
	for word in possible:
		# tally the frequencies of each letter in this set of words
		for letter in word:
			# if letter not in letters: continue
			if letter not in letterFreqs:
				letterFreqs[letter] = 0
			letterFreqs[letter] += 1

	# determine the letter that appears the most
	for letter,frequency in letterFreqs.items():
		# that isn't one already guessed
		if letter in guessedLetters:
			continue
		elif frequency > max:
			max = frequency
			maxLetter = letter

	return maxLetter
