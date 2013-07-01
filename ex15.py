from sys import argv

script,filename = argv

txt = open(filename)

print "This is the contents of your filename : %r" % filename
print txt.read()

print "Type the filename again :  "
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()