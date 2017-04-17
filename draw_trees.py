import codecs
from collections import Counter
count = {}
with codecs.open('./ICres.txt', 'r', encoding='utf-8', errors='ignore') as f:
	for line in f:
		l = line.split(' ')
		if(len(l)>1):
			if l[0]+' -> '+l[1] not in count:
				count[l[0]+' -> '+l[1]] = 1
			else:
				count[l[0]+' -> '+l[1]] += 1


fr = open('./ICres_trees.txt', 'w', encoding='utf-8')
for i in count:
	if count[i] > 50:
		fr.write(str(i)+'\n')

fr.close()


