.PHONY: default

default : testDrive.py
		chmod +x testDrive.py
		python testDrive.py

view : 
		less record.py
		less myCSV.py
		less testDrive.py
