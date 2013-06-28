x = "There are %r kinds of people in the world" %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s know %s" %(binary,do_not,binary)

print x
print y

print "I said : %r " %x
print "I also said : %r" %y

the_false = False
sentence = "Are you lying to me ? %r"

print sentence % the_false