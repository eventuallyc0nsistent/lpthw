# Game Idea :
# You walk into a room filled with teddy bears. 
# You are asked to pick the red or blue one.
# The red one will make you fall in love
# 	Then you walk to a pretty girl wearing a red dress.
# 	You are asked to do one of the following :
# 		1. kiss her
# 		2. drag her to your house

# 	When you kiss her you are super human 
# 	When you drag her home, she turns into a werewolf and she kills you.

# The blue one will take you to your ex-gf
# 	You have two choices then .
# 		1. run
# 		2. cry
# 	When you run away you go back to the beginning of the game.
# 	When you cry you are stuck with her forever and are never free

def love():
	print "You walk into a girl wearing a red dress"
	print "You can either kiss her or drag her to your house"
	print "What do you choose ?"

	lover_pick = raw_input("> ")

	if lover_pick == "kiss":
		print "You are super human"
	elif lover_pick == "drag" :
		dead("She turns into a werewolf and kills you")

def goto_ex():
	print "You are now in front of your ex-gf"
	print "You can either run or cry"
	print "What do you do ?"

	ex_pick = raw_input("> ")

	if ex_pick == "run":
		start()
	elif ex_pick == "cry" :
		dead("You are stuck with her forever ! Good luck.")

def dead(why):
	print why

def start ():
	print "You walk into a room filled with teddy bears"
	print "You can either take the red teddy bear or the blue teddy bear"
	print "Which one do you pick ?"

	teddy_pick = raw_input("> ")

	if teddy_pick == "red" :
		love()
	elif teddy_pick == "blue" :
		goto_ex()
	else :
		print "\n--------------You are a man without decisions, try again!---------------------\n"
		start()

start()