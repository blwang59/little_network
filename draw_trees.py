import codecs
import json
from collections import Counter
count = {}

network = json.load(open('./network_final.json'))
with codecs.open('./ICres_time.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        l = line.split(' ')
        if(len(l)>1):
            if l[1] not in count:
                count[l[1]] = 1
            else:
                count[l[1]] += 1
count_final={}
for i in count:
    if count[i] > 50:
                count_final[i] = count[i]
                
maxnode = {}
for i in network:
        for j in network[i]:
                if j in count_final:
                        if j not in maxnode:
                                maxnode[j] = i
                        elif network[i][j]> network[maxnode[j]][j]:
                                maxnode[j] = i


fr = open('./ICres_tree_final.txt', 'w')
fr.write('digraph G{')
for i in maxnode:
    fr.write(maxnode[i]+' -> '+i+'\n')
fr.write('}')
fr.close()


