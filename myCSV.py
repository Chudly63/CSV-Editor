#!/usr/bin/python
# Record: container for a list of fields.
# 
# Alex M Brown
# Started: 1/31/17 
# Completed: TBD

import sys
from record import Record

class MyCSV:

	def __init__( self, csvFile, sep, esc, new ):
		self.file = csvFile
		self.records = []
		if sep == esc:
			print "Separator cannot equal Escaped Character\nUsing defaults"
			self.sep = ','
			self.esc = '\\'
		else:
			self.sep = sep
			self.esc = esc
		if not new:
			self.readFile()
		else:
			open(csvFile, 'w').close()
		

	#Takes in a list and sorts it. Each swap made in the list is made in the
	#records
	def sort(self, val):
		for r in val:
			for c in range(0,len(val) - 1):
				if val[c] > val[c+1]:
					hold = val[c]
					val[c] = val[c+1]
					val[c+1] = hold
					self.swapRecords(c, c+1)

	#Sorts the CSV alphabetically by the field designated by index
	def sortCSV(self, index):
		values = []
		for r in self.records:
			if len(r.fields) < index:
				print "Invalid Field Index (1)"
				return False
			else:
				values.append(r.fields[index])
		self.sort(values)

	#Swaps the positions of two records
	def swapRecords(self, index1, index2):
		hold = self.records[index1]
		self.records[index1] = self.records[index2]
		self.records[index2] = hold
		

	#Adds a new record to records[]
	def addRecord(self, index, value):
		if len(self.records) < index or index < 0:
			print "Invalid Record Index"
			return False
		else:
			r = Record(value, self.sep, self.esc)
			self.records.insert(index, r)
			return True

	#Removes a record from records[]
	def removeRecord(self, index):
		if len(self.records) < index or index < 0:
			print "Invalid Record Index"
		else:
			self.records.remove(self.records[index])


	#Adds a field in the selected record
	def addField(self, index1, index2, value):
		if len(self.records) < index1 or index1 < 0:
			print "Invalid Record Index"
		else:
			self.records[index1].addField(index2, value)		

	
	#Changes a field in the selected record
	def setField(self, index1, index2, value):
		if len(self.records) < index1 or index1 < 0:
			print "Invalid Record Index"
		else:
			self.records[index1].setField(index2, value)		


	#Removes a field in the selected record
	def removeField(self, index1, index2):
		if len(self.records) < index1 or index1 < 0:
			print "Invalid Record Index"
		else:
			self.records[index1].removeField(index2)		


	#Prints all values in a CSV in a simple table
	def printCSV( self ):
		recordNum = 0
		print "----------------------------------------------------"
		for r in self.records:
			print str(recordNum) + "|",
			r.printRecord()
			recordNum += 1
		print "----------------------------------------------------"


	#Updates the CSV file with the information added during the session
	def writeFile( self ):
		writer = open(self.file, 'w')
		for r in self.records:
			writer.write(r.base + "\n")
		writer.close()
		

	#Splits the file by line and creates records for each line
	def readFile( self ):	
		with open(self.file) as f:
			temp = f.read().splitlines()

		self.records = []

		for line in temp:
			d = Record(line, self.sep, self.esc)
			self.records.append(d)


	#Sets the separator
	def setSep(self, sep):
		if sep == self.esc:
			print "Separator must not equal Escaped Character"
		else:
			for r in self.records:
				r.setSep(sep)


	#Sets the escaped character
	def setEsc(self, esc):
		if esc == self.sep:
			print "Escaped Character must not equal Separator"
		else:
			for r in self.records:
				r.setEsc(esc)

	
	def getField(self, index1, index2):
		if len(self.records) < index1 or index1 < 0:
			print "Invalid Record Index"
		elif len(self.records[index1].fields) < index2 or index2 < 0:
			print "Invalid Field Index"
		else:
			return self.records[index1].fields[index2]
	


