def add(a,b):
	print "Adding %d + %d :" %(a,b)
	return a+b

def sub(a,b):
	print "Subtracting %d - %d :" %(a,b)
	return a-b

def multipy(a,b):
	print "Multiplying %d * %d :" %(a,b)
	return a*b

def divide(a,b) :
	print "Dividing %d / %d : " %(a,b)
	return a/b


print "Lets do some math"

age = add(30,20)
height = sub(10,30)
weight = multipy(40,20)
iq = divide(3,2)

print "Age : %d \nHeight : %d \nWeight : %d \nIQ : %d" %(age,height,weight,iq)

print "Lets do some funny math:"
something = add(age,sub(height,multipy(iq,weight)))

print "THis is weird : %d" %something