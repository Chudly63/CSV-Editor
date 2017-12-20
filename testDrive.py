#!/usr/bin/python
# 
# 
# 
#

import sys
#from record import Record
from myCSV import MyCSV

def main( argv=sys.argv ) :
	
	#testCSV = MyCSV('doc3.csv', ',', '*', True)
	#testCSV.addField(0,0,'Brown, Alex')
	#testCSV.addField(0,1,'M')
	#testCSV.setField(0,1,'F')
	#testCSV.removeField(0,1)
	#testCSV.printCSV()
	#testCSV.writeFile()

	print "\n\nALEX M BROWN's SUPER AMAZING CSV MANAGER"
	print "\n\nSelect an Option"
	print "1. Make a New CSV File"
	print "2. Open an Existing CSV File"
	op = ""
	while not op == '1' and not op == '2':
		op = raw_input('Selection: ')
	name = raw_input('Enter filename: ')
	sep = ""
	esc = ""
	while not len(sep) == 1:
		sep = raw_input('Enter Separating Character: ')
	while not len(esc) == 1:	
		esc = raw_input('Enter Escaped Character: ')
	CSV = MyCSV(name, sep, esc, op == '1')
	op = ""
	while not op == '0':
		op = ""
		print "\n\n\n"
		CSV.printCSV()
		print "\n\nSelect an Option"
		print "1. Change a Field"
		print "2. Add a Field"
		print "3. Remove a Field"
		print "4. Add a Row"
		print "5. Remove a Row"
		print "6. Sort Records"
		print "0. Save and Quit"
		print op
		while not op == '0' and not op == '1' and not op == '2' and not op == '3' and not op == '4' and not op == '5' and not op == '6':
			op = raw_input('Selection: ')
		if op == '0':
			CSV.writeFile()
		elif op < '4':
			index1 = raw_input("Enter Row Pos: ")
			index2 = raw_input("Enter Field Pos: ")
			if not op == '3':
				val = raw_input("Enter Field Value: ")
				if op == '1':
					CSV.setField(int(index1), int(index2), val)
				else:
					CSV.addField(int(index1), int(index2), val)
			else:
				CSV.removeField(int(index1), int(index2))
		elif op < '6':
			row = raw_input("Enter Ros Pos: ")
			if op == '4':
				val = raw_input("Enter Row Data: ")
				CSV.addRecord(int(row), val)
			else:
				CSV.removeRecord(int(row))
		else:
			fl = raw_input("Enter Field # To Sort By: ")
			CSV.sortCSV(int(fl))
		

	

if __name__ == "__main__" :
	# then this was NOT included in another file, so, run the test driver
	main()

