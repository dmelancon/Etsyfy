import sys
import re
fullcode = []
asciiBorder = open('asciiArt/ascii.txt', 'r');
asciiSkull = open('asciiArt/skull.txt', 'r');
asciiCat = open('asciiArt/cat.txt', 'r');
asciiFill = open('asciiArt/fill.txt', 'r');
code = open(sys.argv[1], 'r');


art = []
codeLines = [] 
skull = []
cat = []
fill = []
#find longest line of ASCII Art

longestArtLine = 0
for line in asciiBorder:
	if len(line) > longestArtLine:
		longestArtLine = len(line)
	if len(line)>1:
		art.append(line[:-1])
	elif len(line)==1:
		art.append(line)
#print longestArtLine

#longest line of code
longestLine = 0

for line in code:
	if len(line) > longestLine:
		longestLine = len(line)
	if len(line)>1:
		codeLines.append(line)
for line in asciiSkull:
	if len(line)>1:
		skull.append(line)
for line in asciiCat:
	if len(line)>1:
		cat.append(line)
for line in asciiFill:
	if len(line)>1:
		fill.append(line)

artHead = art[:9]
for line in artHead:
	print line 
#print Art Body

artBody = art[11:21]
for line in artBody:
	length = longestArtLine-(len(line)*2)
	space = ''
	for i in range(25,length):
		space = space+'*'
	print line  +'//'+ space+line

#print repeating artBody pattern appened before and after code
def insert(codeToInsert, isCode): 
	value  = int
	for idx,val in enumerate(codeToInsert):
		artLine = artBody[idx%10]
		artWidth = len(artLine)
		codeWidth = len(codeToInsert[idx%10])
		spaceWidth = longestArtLine-(longestLine-2*artWidth)
		space = ''
		for i in range(5,spaceWidth-len(val)):
			space = space + '*'
		if len(val)>1:
			if isCode:
				print artLine+val[:-1]+'//'+space+artLine
			else:
				print artLine+val[:-1]+'**'+space+artLine
		else:
			if isCode:
				print artLine+val+'//'+space[:-1]+artLine
			else:
				print artLine+val[:-1]+'**'+space+artLine
	return

insert(fill, 0)
insert(skull,0)
insert(fill,0)
insert(codeLines,1)
insert(fill,0)
insert(cat,0)
insert(fill,0)

#finish out the pattern
for line in artBody[len(cat):]:
	length = longestArtLine-len(line)*2
	space = ''
	for i in range(25,length):
		space = space+'*'
	print line + space + line
#onemore
for line in artBody:
	length = longestArtLine-len(line)*2
	space = ''
	for i in range(25,length):
		space = space+'*'
	print line +'//'+ space + line

#transition to footer
for line in artBody[:3]:
 	length = longestArtLine-len(line)*2
	space = ''
	for i in range(25,length):
		space = space+'*'
	print line +'//'+ space +line

# print artFooter
artFooter = art[-9:]
for line in artFooter:
	print line