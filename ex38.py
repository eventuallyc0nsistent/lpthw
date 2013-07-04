ten_things = "Apple Mango Hero Grape Banana Lion Tiger"

print "Wait we need 10 things"

stuff = ten_things.split(' ')
more_things = ["Gorilla","Chimpanzee","Day",24]

while len(stuff) !=10 :
	next_one = more_things.pop()
	print "Adding next element : %r" % next_one
	stuff.append(next_one)
	print "We have %d elements now" %len(stuff)

print "This is the list of elements :",stuff
