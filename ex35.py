from sys import exit

def gold_room():
	print "There is gold in the room. Soo soo much gold. How much do you want to take ?"
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else :
		dead("Do you even type, bro ?")

	if how_much<50:
		print "Nice you're not greedy. You win !"
		exit(0)
	else :
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here"
	print "The bear has honey"
	print "The fat bear is in front of another door"
	print "How are you going to move the bear ?"
	bear_moved=False

	while True :
		next = raw_input("> ")

		if next=="take honey":
			dead("The bear is angry and kills you")
		elif next=="taunt bear" and not bear_moved:
			print "The bear has moved now you can go"
			bear_moved = True
		elif next=="open door" and bear_moved :
			gold_room()
		else :
			print("I have no idea what it means")

def cthulu_room():
	print "Here you see the evil Cthulu"
	print "He, it, whatever stares at you and goes insane"
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next :
		start()
	elif "head" in next :
		dead("Well thats sad & tasty")
	else :
		cthulu_room()

def dead(why):
	print why,"Right on !"
	exit(0)

def start():
	print "You are in a dark room"
	print "There is a door to your right and left"
	print "Which door do you take ?"

	next = raw_input("> ")
	
	if next == "left" :
		bear_room()
	elif next == "right" :
		cthulu_room()
	else :
		dead ("And this ends cause of you acting smart")

start()