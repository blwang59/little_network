import codecs
import json
# import sys
# sys.setrecursionlimit(10000)
from collections import Counter
count = {}

# network = json.load(open('./network_final.json'))
with codecs.open('./inter_res/ICres.txt', 'r', encoding='utf-8', errors='ignore') as f:
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
        count_final[i]=count[i]

print(count_final.items())


with codecs.open('./inter_res/ICres.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        l = line.split(' ')
        if(len(l)>1) and l[1] in count_final:
            count_final[l[1]] = l[0]





# count_final={}
# for i in count:
#     if count[i] > 50:
#                 count_final[i]=count[i]
# #print(count_final.keys())
                
# maxnode = {}
# # for i in network:
# #     for j in network[i]:
# #             if j in count_final:
# #                 if j not in maxnode:
# #                     maxnode[j] = i
# #                 elif network[i][j]> network[maxnode[j]][j]:
# #                     maxnode[j] = i
# #                 else:
# #                     pass

# def find_source(node):
#     maxn = 0
#     res = ""
#     for i in network:
#         for j in network[i]:
#             if j==node:
#                 if network[i][j]>maxn:
#                   maxn = network[i][j]
#                   res = i
#     return res

#     # res = ""
#     # for i in network[node]:
#     #     if network[i][node] > maxn:
#     #         maxn = network[i][node]
#     #         res = i

#     # return res



# def draw(nodeset):
#     for node in nodeset:
#         if find_source(node) not in nodeset:
#             nodeset[node] = find_source(node)
#             return draw(nodeset)
                
# # for node in count_final:






# draw(count_final)

# print(count_final.items())


#     # for i in network[node][i]:
#     #     if i not in maxnode:
#     #         maxnode[node]=i
#     #     elif network[i][node]>network[maxnode[node]][node]:
#     #         maxnode[node]=i




# fr = open('./ICres_tree_final.txt', 'w')
# fr.write('digraph G{\n')
# for i in maxnode:
#     fr.write(i+'\n')
# fr.write('}')
# fr.close()
name_author={}
with codecs.open('./inter_res/author_with_aff.txt', 'r', encoding='utf-8', errors='ignore') as f1:
    for line in f1:
        items = line.rstrip().split(' ', 2)
        names=items[2].split(':')
        name=names[0]
        name_author[items[0]] = name

fr = open('./results/ICres1.dot', 'w')
fr.write('digraph G{\n')
for i in count_final:
    fr.write('"'+name_author[count_final[i]]+'"'+' -> '+'"'+name_author[i]+'"'+'\n')
fr.write('}')
fr.close()