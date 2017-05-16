import codecs
import json
mess = {}
size = 0
sizeo = 0
network= {}
len_net = 0


index_of_author = {}


def add_networks(dic1, key_a, key_b, val):
    if key_a in dic1:
        dic1[key_a].update({key_b: val})
    else:
        dic1.update({key_a: {key_b: val}})

with codecs.open('./inter_res/author_with_aff_sorted.txt', 'r', encoding='utf-8', errors='ignore') as f1:
    for line in f1:
        items = line.rstrip().split(' ', 2)
        index_of_author[items[2]] = items[0]

# print(index_of_author)

with codecs.open('../../aminernetwork/AMiner-Paper.txt', 'r', encoding='utf-8', errors='ignore') as f:
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
                for j in range(min(size,sizeo)):
                    # print('1')
                    if mess['#@'+str(i)]+':'+mess['#o'+str(i)] in index_of_author and \
                        mess['#@' + str(j)] + ':' + mess['#o' + str(j)] in index_of_author and mess['#o'+str(i)] != '' and mess['#o'+str(j)] != ''\
                        and index_of_author[mess['#@'+str(i)]+':'+mess['#o'+str(i)]] < index_of_author[mess['#@'+str(j)]+':'+mess['#o'+str(j)]]:
                       

                        if mess['#@'+str(i)]+':'+mess['#o'+str(i)]  not in network \
                        or mess['#@'+str(j)]+':'+mess['#o'+str(j)] not in network[mess['#@'+str(i)]+':'+mess['#o'+str(i)]]:

                            add_networks(network,mess['#@'+str(i)]+':'+mess['#o'+str(i)],mess['#@'+str(j)]+':'+mess['#o'+str(j)],1)
                            # add_networks(network,mess['#@' + str(j)] + ':' + mess['#o' + str(j)],mess['#@' + str(i)] + ':' + mess['#o' + str(i)], 1)
                        else: 
                            network[mess['#@'+str(i)]+':'+mess['#o'+str(i)]][mess['#@'+str(j)]+':'+mess['#o'+str(j)]]+=1
                            # network[mess['#@'+str(j)]+':'+mess['#o'+str(j)]][mess['#@'+str(i)]+':'+mess['#o'+str(i)]]+=1 



            mess = {}

            size = 0
            sizeo = 0



fr = open('./inter_res/network_dict_with_conumbers.json', 'w',encoding = 'utf-8',errors='ignore')
json.dump(network,fr,ensure_ascii=False)

