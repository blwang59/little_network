import codecs
import json
mess = {}
size = 0
sizeo = 0
network= {}
len_net = 0
index_of_author = {}
papers_per_author ={}
def add_networks(dic1, key_a, key_b, val):
    if key_a in dic1:
        dic1[key_a].update({key_b: val})
    else:
        dic1.update({key_a: {key_b: val}})

with codecs.open('./author_with_aff.txt', 'r', encoding='utf-8', errors='ignore') as f1:
    for line in f1:
        items = line.rstrip().split(' ', 2)
        index_of_author[items[2]] = items[0]
        # papers_per_author[items[0]] = items[1]


#print (index_of_author.items())


#print (papers_per_author.items())

        

# network = [[0 for col in range(0, len_net)] for row in range(0, len_net)]
#
with codecs.open('./AMiner-Paper.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if line != '\n':
            line1 = line[:-1].split(' ', 1)
            if len(line1) <= 1:
                continue
            line2 = line1[1].split(';')
            for i in range(0, len(line2)):
                mess[line1[0]+str(i)] = line2[i]

        if line[:2] == '#@':
            size = len(line[3:-1].split(';'))
        if line[:2] == '#o':
            sizeo = len(line[3:-1].split(';'))
        if line == '\n':

            for i in range(min(size,sizeo)):
                for j in range(i+1,min(size,sizeo)):
                    if str(mess['#@'+str(i)]+':'+mess['#o'+str(i)]) in index_of_author and \
                                            str(mess['#@' + str(j)] + ':' + mess['#o' + str(j)]) in index_of_author:
                     
                   
                        if str(index_of_author[mess['#@'+str(i)]+':'+mess['#o'+str(i)]]) not in network or \
                                    str(index_of_author[mess['#@'+str(j)]+':'+mess['#o'+str(j)]]) not in network or \
                                     str(index_of_author[mess['#@'+str(i)]+':'+mess['#o'+str(i)]]) not in network[str(index_of_author[mess['#@'+str(j)]+':'+mess['#o'+str(j)]])] or \
                                     str(index_of_author[mess['#@'+str(j)]+':'+mess['#o'+str(j)]]) not in network[str(index_of_author[mess['#@'+str(i)]+':'+mess['#o'+str(i)]])]:
                            add_networks(network,str(index_of_author[mess['#@'+str(i)]+':'+mess['#o'+str(i)]]),str(index_of_author[mess['#@'+str(j)]+':'+mess['#o'+str(j)]]),1)
                            add_networks(network, str(index_of_author[mess['#@' + str(j)] + ':' + mess['#o' + str(j)]]),str(index_of_author[mess['#@' + str(i)] + ':' + mess['#o' + str(i)]]), 1)
                        else:
                            
                            network[str(index_of_author[mess['#@'+str(i)]+':'+mess['#o'+str(i)]])][str(index_of_author[mess['#@'+str(j)]+':'+mess['#o'+str(j)]])] += 1
                            network[str(index_of_author[mess['#@' + str(j)] + ':' + mess['#o' + str(j)]])][
                                str(index_of_author[mess['#@' + str(i)] + ':' + mess['#o' + str(i)]])] += 1

            mess = {}

            size = 0
            sizeo = 0

# for i in network:
#     for j in i:
#         network[i][j]=int(network[i][j])/int(papers_per_author[j])    



fr = open('./network_dict_test.json', 'w',encoding = 'utf-8',errors='ignore')
json.dump(network,fr)

# fr.close()
# for author1 in network:
#     fr.write(str(author1.key())+' ')
#     for author2 in author1:
#         fr.write(str(author2.key())+':'+str(network[author1][author2]))
#     fr.write('\n')
# fr.close()
#
#        # print(index_of_author.items())


# with open('network_dict.json','a') as outfile:
#     json.dump(network,outfile)