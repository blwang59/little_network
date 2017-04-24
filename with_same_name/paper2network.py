# coding:UTF-8
import codecs
import json

class Node:
    def __init__(self, name, times=0):
        self.name = name
        self.times = times


class Graph:
    def __init__(self):
        self.net = []
        self.node = []
        # elements in list node[] are all Node()!

    def add_node_by_name(self, name, time):
        node = Node(name, time)
        self.node.append(node)

    def con_net(self):
        # self.net = []
        for i in range(0, len(self.node)):
            tmp = []
            for j in range(0, len(self.node)):
                tmp.append(0)
            self.net.append(tmp)

    def assign_net(self, name1, name2):
        self.node[self.node.index(name1)][self.node.index(name2)] += 1

    def print_net(self):
        #fnet = open('C:/Users/Administrator/Desktop/net.txt', 'w', encoding='utf-16')
        for i in range(0, len(self.node)):
            for j in range(0, len(self.node)):
                fnet.write(str(self.node[i][j]))
            fnet.write('\n')
        fnet.close()
author_dict = {}
network_dict = {}
first_time = {}
mess = {}
def add_networks(dic, key_a, key_b, val):
    if key_a in dic:
        dic[key_a].update({key_b: val})
    else:
        dic.update({key_a: {key_b: val}})
# f1 = open('C:/Users/Administrator/Desktop/net.txt', 'w', encoding='utf-16')
with codecs.open('../AMiner-Paper.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if line != '\n':
            l = line.rstrip().split(' ',1)
            if len(l) > 1:
                mess[l[0]] = l[1]
        if line == '\n':
            if '#@' in mess and '#t' in mess and mess['#t'].isdigit():
                authors = mess['#@'].split(';')
                for a in authors:
                    if a not in first_time or int(mess['#t']) < first_time[a]:
                        first_time[a] = int(mess['#t'])
                    if a not in author_dict:
                        author_dict[a] = 1
                    else:
                        author_dict[a] += 1
            mess={}


with codecs.open('../AMiner-Paper.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if line[:2] == '#@':
            authors = line[3:-1].split(';')
            if len(authors) > 1:
                for author in authors:
                    for author2 in authors:
                        if author in author_dict and author2 in author_dict\
                        and author_dict[author]>5 and author_dict[author2]>5 \
                        and first_time[author] < first_time[author2]\
                        and authors.index(author) > authors.index(author2):
                            if author not in network_dict or author2 not in network_dict[author]:
                                add_networks(network_dict, author, author2, 1)
                                # add_networks(network_dict, author2, author, 1)
                                
                            else:
                                network_dict[author][author2] += 1
                                # network_dict[author2][author] += 1


for i in network_dict:
    for j in network_dict[i]:
        network_dict[i][j] = network_dict[i][j]/int(author_dict[j])

fr = open('./inter_res/network_withsamename_sorted_0424.json', 'w',encoding = 'utf-8',errors='ignore')
json.dump(network_dict,fr,ensure_ascii=False)



