import re
import sys
file_name=sys.argv[1]
with open(file_name,"r") as s:
# 	data=s.read().replace('\n', '')
	content=s.read().splitlines()
	val=content[0].strip()
	(year,temp)=(val[1:6],val[10:12])
	print('year is ',year)
#	print(data)
#	line=s.read()
#	print (line)
#	val = line.strip()
#	print (val)
#	(year, temp, q) = (val[15:19], val[87:92], val[92:93])
#	if (temp != "+9999" and re.match("[01459]", q)):
#		print "%s\t%s" % (year, temp)
#content=[x.strip() for x in content]
print (content)
print('len(content) is ',len(content))

for val in content:
	data=val
