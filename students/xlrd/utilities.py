from xlrd import cellname, cellnameabs, colname

print cellname(0,0),cellname(10,10),cellname(100,100)
print cellnameabs(3,1),cellnameabs(41,59),cellnameabs(265,358)
print colname(0),colname(10),colname(100)
