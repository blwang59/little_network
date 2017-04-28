import codecs
import json
# import sys
# sys.setrecursionlimit(10000)
from collections import Counter
count = {}
edge_count = {}
# network = json.load(open('./network_final.json'))
with codecs.open('./inter_res/ICres.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        l = line.split(' ')
        if(len(l)>1):
            if l[1] not in count:
                count[l[1]] = 1
            else:
                count[l[1]] += 1

        if len(l)>1:
            if l[0]+'->'+l[1] not in edge_count:
                edge_count[l[0]+'->'+l[1]] = 1
            else: 
                edge_count[l[0]+'->'+l[1]] += 1

count_final={}
for i in count:
    if count[i] > 50:
        count_final[i]=count[i]

#saving the most influenced edge for each node:
edge = {}
for item in edge_count:
    node_end = item.split('->')[1]
    node_start = item.split('->')[0]
    if node_end not in edge or edge_count[item]>edge_count[edge[node_end]+'->'+node_end]:
        edge[node_end] = node_start




# print(count_final.items())


with codecs.open('./inter_res/ICres.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        l = line.split(' ')
        if(len(l)>1) and l[1] in count_final:
            count_final[l[1]] = l[0]

name_author={}
with codecs.open('./inter_res/author_with_aff.txt', 'r', encoding='utf-8', errors='ignore') as f1:
    for line in f1:
        items = line.rstrip().split(' ', 2)
        names=items[2].split(':')
        name=names[0]
        name_author[items[0]] = name




fr = open('./results/ICres_0422_withname(JiaweiHan).dot', 'w')
fr.write('digraph G{\n')
for i in count_final:
    fr.write('"'+name_author[count_final[i]]+'"'+' -> '+'"'+name_author[i]+'"'+'\n')
    # fr.write(count_final[i]+' -> '+i+'\n')

for i in edge:
    fr.write('"'+name_author[edge[i]]+'"'+' -> '+'"'+name_author[i]+'"'+'\n')
fr.write('}')
fr.close()