ten_things = "Apple Mango Hero Grape Banana Lion Tiger"

print "Wait we need 10 things"

stuff = ten_things.split(' ')
more_things = ["Gorilla","Chimpanzee","Day"]

while len(stuff) !=10 :
	next_one = more_things.pop()
	print "Adding next element : %r" % next_one
	stuff.append(next_one)
	print "We have %d elements now\n" %len(stuff)

print "This is the list of elements :",stuff

print stuff[-1]
print stuff.pop(3)
print ' '.join(stuff)
print '#'.join(stuff[3:5])