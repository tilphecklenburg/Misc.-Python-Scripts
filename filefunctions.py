#-------import required modules for functions below----------------------
from openpyxl import Workbook
#------------------------------------------------------------------------

#-------create a new Excel workbook using OpenPyxl-----------------------
def createexceldoc(filename):
	exceldoc = Workbook()
	print "workbook created"
	excelsheet = exceldoc.create_sheet(title = "Sheet")
	return excelsheet
#------------------------------------------------------------------------	

#-------search for string in a .txt file---------------------------------
def searchtextfile(filename,searchphrase,reportsheet):
	rowcount = 1
	file = open(filename,"r+")
	for line in file.readlines():
		if searchphrase in line:
			reportsheet['A' + str(rowcount)] = searchphrase
			reportsheet['B' + str(rowcount)] = line
			rowcount += 1
#------------------------------------------------------------------------	

#-------open text file and turn into a list------------------------------
def parsetextfiletolist(filename):
	file = open(filename,"r+")
	list = file.read()
	list = list.split()
	return list
#------------------------------------------------------------------------