from sys import argv
from os.path import exists


script, from_file , to_file = argv

print "Copying %r to %r " %(from_file,to_file)

in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long" %len(in_data)
print "Checking for output file if it exists %r" % exists(to_file)
print "ENTER to continue, CTRL - C to exit"
raw_input()

out_file = open(to_file,'w')
out_file.write(in_data)

print "DONE !"
in_file.close()
out_file.close()