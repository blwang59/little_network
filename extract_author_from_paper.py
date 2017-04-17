import codecs


class Node:
    def __init__(self, name='', aff=''):
        self.name = name
        self.aff = aff

    def print_node(self):
        print(self.name+':'+self.aff)

    def write_into(self):
        return self.name+':'+self.aff


def node_list_append(list1, node):
    if node not in list1:
        list1.append(node)
    else:
        pass

fres = codecs.open('C:/Users/Administrator/Desktop/authors_from_paper.txt', 'w', encoding='utf-16')
network_dict = {}
author_aff = []
author_list=[]
author_l=[]
aff_l=[]
with codecs.open('E:/Aminer/Aminer-Paper.txt', 'r', encoding='utf-16', errors='ignore') as f:
    for line in f:

            if line[:2] == '#@':
                authors = line[3:-1].split(';')
                for author in authors:
                    author_l.append(author)
            if line[:2] == '#o':
                affs = line[3:-1].split(';')
                for aff in affs:
                    aff_l.append(aff)

            if line == '\n':

                for i in range(len(author_l)):
                    node_list_append(author_list, Node(author_l[i], aff_l[i]))
                author_l = []
                aff_l = []

            #for item in author_list:






             #   item.print_node()


for items in author_list:

    fres.write(items.write_into())
    fres.write('\n')
fres.close()


