print "You enter a dark room with two doors. Which door do you pick ? Door1 or Door2 ?"

door = raw_input("> ")

if door == "1" :
	print "There is a giant bear here eating a cheese cake. What do you do ?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face. Sucker!"
	elif bear == "2":
		print "The bear eats your leg off. Ouch!"
	else :
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2" :
	print "You stare into the endless abyss at the Cthulhu's retina"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understandin revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2" :
		print "Your body survives powered by a mind of jello. Wonderful !"
	else :
		print "The insanity rots your eyes into a pool of much. Good job!"

else :
	print "You stumble and fall on a knife , cut yourself and die. Good day !"