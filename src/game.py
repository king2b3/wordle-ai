import random, pickle as pkl
from collections import defaultdict
wordList = pkl.load( open( "words.p", "rb" ) )

bcolors = {
    'GREEN': '\033[92m',
	'YELLOW': '\033[93m',
    'ENDC': '\033[0m',
}



def def_value():
    return 0
      
class Game():
	def __init__(self):
		self.word = random.choice(wordList)
		self.letters = defaultdict(def_value)
		for l in self.word:
			self.letters[l] += 1
		#print(self.word)
	
	def checkword(self, guess) -> list:
		temp = ""
		temp_dict = defaultdict(def_value)
		if guess == self.word:
			return "win"
		else:
			for l in range(len(guess)):
				temp_dict[guess[l]] += 1
				if guess[l] == self.word[l]:
					temp += f"{bcolors['GREEN']}{guess[l]}{bcolors['ENDC']}"
				elif guess[l] in self.word:
					if temp_dict[l] > self.letters[l]:
						temp += f"{guess[l]}"
					else:
						temp += f"{bcolors['YELLOW']}{guess[l]}{bcolors['ENDC']}"					
				else:
					temp += f"{guess[l]}{bcolors['ENDC']}"
			return temp
	
	def check(self, guess):
		while guess not in wordList or len(guess) != 5:
			print(f"invalid word")
			guess = input()
			guess.strip()
		return self.checkword(guess)


import os
def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

game = Game()
history = f"Welcome to Wordle\n"
for turn in range(1,7):
	clearScreen()
	print(history)
	print(f"turn:{turn}")
	g = input()
	g.strip()
	if (temp := game.check(g)) == "win":
		print(f"YOU WIN")
		exit()
	if temp:
		history += temp + '\n'
print(f"THE WORD IS {game.word}")
print(f"YOU LOSE. SAD")

