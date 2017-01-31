from fmcapifunctions import getdomainuuid
from fmcapifunctions import postnewobject

print """

Thank you for using the FMC network object import tool, and please note the following:

No support will be provided for this script, it is presented as-is and features may or may not be added in future versions.
The creator is not responsible for any downtime incurred or misconfiguration applied on customer systems; development, production or otherwise.

"""

username = raw_input("Enter FMC username>>> ")
password = raw_input("Enter FMC password>>> ")
filename = raw_input("""

Enter name of CSV file to import objects from, should be in the same dir as this EXE,
and please note the required format:
" objectname,object value (the address corresponding to the object),a short description for object, and object type (host, network, etc.) " 

CSV File>>>""")

server = raw_input("""

Enter host name or IP of FMC:

FMC Host name or IP>>>""")
domainuuid = getdomainuuid(server,username,password)
csvfile = open(filename,"r+")

rawtext = csvfile.read()

rawtext = rawtext.split("\n")

for line in rawtext:
	line = line.split(",")
	postnewobject(server,domainuuid,username,password,str(line[0]),str(line[1]),str(line[2]),str(line[3]))
	