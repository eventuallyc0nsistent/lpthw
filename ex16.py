from sys import argv

script, filename = argv

print "Erasing file : %r" %filename

print "Opening file :"
new_file = open(filename,'w')

print "Truncation File"
new_file.truncate()

print "Input lines: "
line1 = raw_input("line1>")
line2 = raw_input("line2>")
line3 = raw_input("line3>")

print "Now writing to file"
new_file.write(line1)
new_file.write("\n")
new_file.write(line2)
new_file.write("\n")
new_file.write(line3)

print "closing file"
new_file.close()