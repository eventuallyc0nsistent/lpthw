def cheese_and_crackers(cheese_count,crackers_count):
	print "\n"
	print "Cheese count : %d" %cheese_count
	print "Crackers count : %d" %crackers_count
	print "\n"

cheese_and_crackers(20,40)

cheese_number = 3
cracker_number = 4

print "Printing from variables:"
cheese_and_crackers(cheese_number,cracker_number)

print "Doing math inside:"
cheese_and_crackers(10+30,10)

print "Combine math & variables:"
cheese_and_crackers(cheese_number + 10, cracker_number - 5)

