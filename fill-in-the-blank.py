#Choose Level of the game

def choose_level():
	prompt = "Please choose a difficulty (Easy, Medium, or Hard): "
	difficulty = raw_input(prompt)
	level = difficulty.lower()
	choices = ['easy', 'medium', 'hard']	#The user's options for difficulty
	
	#Making sure the user inputs the right difficulty

	while not level in choices:
		print "Bad input! Please choose a valid difficulty\n"
		difficulty = raw_input(prompt)
		level = difficulty.lower()

	print "You've chosen " + level + "\n" 

	return level

#Game function

def test(difficulty):

	#Paragraphs will depend on the difficulty the user chose to play

	paragraph = None
	answer = None
	
	#Easy problem prompt

	if difficulty == 'easy':
		paragraph = """His __1__ programming is taking effect. He'll be irresistibly drawn to large __2__ where he'll back up __3__, reverse street signs, and steal everyone's __4__ shoe."""
		answer = ['destructive','cities','plumbing','left']
	
	#Medium problem prompt

	elif difficulty == 'medium':
		paragraph = """Dang it, Jim. I'm an __1__, not a doctor! I mean, I am a doctor, but I'm not that kind of doctor. I have a __2__, it's not the same thing. You can't help __3__ with a doctorate. You just sit there and you're __4__!"""
		answer = ['astronomer','doctorate','people','useless']

	#Hard Problem Prompt

	if difficulty == 'hard':
		paragraph = """Surprised to see me, Crash? Like the __1__ in your fur I keep coming back! Three years I spent alone in the frozen __2__ wastes... and I missed you... and so I've organized a little gathering, like a __3__ party except... the exact opposite. And look, all of your friends are here... you are so very popular. Let's start handing out the __4__."""
		answer = ['fleas','antarctic','birthday','presents']
	

def game(difficulty):
	#Paragraphs will depend on the difficulty the user chose to play
	tries = 5
	count = 0

	# Get quiz text and the answer according to difficulty

    	paragraph = test(difficulty)
    	answer = test(difficulty)

	print "\nYou will get " +str(tries)+ " guesses to solve this puzzle\n"

	print paragraph

	while tries > 0 and count != len(answer):

		#Gets the answer from the user

		guess= raw_input("What should be substituted for __"+str(count+1)+"__?  ")
		
		#Checks if you have the right answer	
		if answer[count].lower() == guess.lower():
			print "Correct\n"

			# if you get the correct answer replace it the blank with the right answer

			paragraph = paragraph.replace("__"+str(count+1)+"__", answer[count])
			print paragraph
			print "Tries left:", tries
			count += 1

		#If you have the wrong answer, print out the tries you have left

		else:
			tries -= 1
			print "\nThat isn't the correct answer! Let's try again; you have " + str(tries) + " tries left:\n"
			print paragraph

		#Checks if you won the game	

		if count == len(answer):
			print finished(tries, count)


def finished(tries, count):
			if count == len(answer):
				print "\nCongrats! You win!\n"
			name = raw_input("Please enter your name ")
			print ("Thank you for playing ") + name 

			#print choose_level()
			#print "Next Round "
			#print game(difficulty)

			#Checks if you lost the game

			if tries == 0:
				print "You Lost! Game Over!\n"
			name = raw_input("Please enter your name ")
			print ("Thank you for playing ") + name
			print "try again "
			print game(difficulty)

#Main Function
if __name__ == '__main__':
    difficulty = choose_level()
    game(difficulty)