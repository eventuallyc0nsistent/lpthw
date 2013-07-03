the_count = [1,2,3,4,5]
fruits = ['apples','mangos','peaches','oranges','kiwi']
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
	print "This is count %d" %number

for fruit in fruits :
	print "The fruit list : %s" %fruit

for i in change :
	print "This is %r " %i

elements = []

for i in range(0,5):
	new_element = raw_input("> ")
	print "Adding %r to the list " %i
	elements.append(new_element)

for i in elements :
	print "%r" %i