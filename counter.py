""" A program that stores and updates a counter using a Python pickle file"""

import os
import sys
from pickle import *

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be reset.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	if os.path.exists(file_name) == True and reset == False:
		file = open(file_name, 'r+')
		old_counter = load(file)
		counter = old_counter + 1
		file.seek(0,0)
		dump(counter, file)
		file.close()

	else:
		file = open(file_name, 'w')
		reset_counter = 1
		dump(reset_counter, file)
		file.close()
	
	final_file = open(file_name, 'r')
	res = load(final_file)
	final_file.close()
	return res

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))