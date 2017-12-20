#!/usr/bin/python
# Record: container for a list of fields.
# 
# Alex M Brown
# Started: 1/28/17 
# Completed: TBD

import sys

class Record:

	def __init__( self, data, sep, esc ):
		self.base = data
		self.sep = sep
		self.esc = esc
		self.splitUp( data, sep, esc )

	def printRecord( self ):
		for r in self.fields:
			print r + "    ",
		print ""

	#Recreates the base string from the stored fields.
	#Used when a field is changed, added, or removed.
	def putTogether( self ):
		bas = "" 
		for r in self.fields:
			for c in r:
				if c == self.sep:
					bas += self.esc + c
				else:
					bas += c
			bas += self.sep
		bas = bas[:-1]	
		self.base = bas

	#Breaks the base string into fields separated by sep.
	def splitUp( self, data, sep, esc ):
		hold = ""
		self.fields = []
		escaped = False
		for c in data:
			if c == esc:
				if escaped:
					hold += c
					escaped = False
				else:
					escaped = True
			elif c == sep and not escaped:
				self.fields.append(hold)
				hold = ""
				escaped = False
			else:
				hold += c
				escaped = False
		self.fields.append(hold)

	#Changes the field stored at index num
	def setField( self, index, value ):
		if len(self.fields) <= index or index < 0:
			print "Invalid Field Index"
		else:
			self.fields[int(index)] = value
			self.putTogether()

	#Add a field at index
	def addField( self, index, value ):
		if len(self.fields) < index or index < 0:
			print "Invalid Field Index"
		elif len(self.fields) == index:
			self.fields.append(value)
			self.putTogether()
		else:
			self.fields.insert(index, value)
			self.putTogether()

	#Remove the field at index
	def removeField( self, index ):
		if len(self.fields) <= index or index < 0:
			print "Invalid Field Index"
		else:
			self.fields.remove(self.fields[index])
			self.putTogether()

	#Changes the separator character. Also re-splits the base string.
	def setSep( self, sep ):
		if sep == self.esc:
			print "Separator cannot be the same as Escaped Character"
		else:
			self.sep = sep
			self.splitUp(self.base, sep, self.esc)

	#Changes the escaped character. Also re-splits the base string.
	def setEsc( self, esc ):
		if esc == self.sep:
			print "Escaped Character cannot be the same as Separator"
		else:
			self.esc = esc
			self.splitUp(self.base, self.sep, esc)


def main( argv=sys.argv ) :
	"Just a test driver - NOT part of the class"

	mom = Record( "Brown>, Alex,19", ',', '>')
	print mom.base
	print mom.sep
	print mom.esc
	print mom.fields

if __name__ == "__main__" :
	# then this was NOT included in another file, so, run the test driver
	main()

