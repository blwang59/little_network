import json
import random
import codecs
network = json.load(open('./inter_res/network_withsamename_sorted_0426_withweight.json'))


def ICmodel(net,seeds,times):

    net=network
    fr = open('./inter_res/ICres_0424.txt', 'w', encoding='utf-8')
    for i in range(times):
        target = []
        active = []
    # for i in net:
    #   for j in net[i]:

    #neighbor_dict = net[seeds]
    #neighbor_q = neighbor_dict.keys()
        #fr = open('./ICres.txt', 'w', encoding='utf-8')
        target.append(seeds)
        active.append(seeds)
        # ltimes = 0
        while(target):
            # ltimes+=1
            node = target.pop()

            #active.append(node)
            if node in net:
                for follower in net[node]:
                    if follower not in active:
                        if random.random() <= net[node][follower]:
                    
                            target.append(follower)
                            active.append(node)
                            fr.write(node + '->' + follower +'\n')

        fr.write('\n')

    fr.close()

def draw_trees(docsource,docdes):
    count = {}
    edge_count = {}
    # count the times which the nodes are activated
    with codecs.open(docsource, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
          l = line.rstrip().split('->',1)
          if(len(l)>1):
              if l[1] not in count:
                  count[l[1]] = 1
              else:
                  count[l[1]] += 1

    # count the times which the edges are activated
    with codecs.open(docsource, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            l = line.rstrip().split('->',1)
            if(len(l)>1):
                if '"'+l[0]+'" -> "'+l[1]+'"' not in edge_count:
                    edge_count['"'+l[0]+'" -> "'+l[1]+'"'] = 1
                else:
                    edge_count['"'+l[0]+'" -> "'+l[1]+'"'] += 1
         


    # count_final={}
    # for i in count:
    #     if count[i] > 50:
    #         count_final[i]=count[i]

    # with codecs.open(docsource, 'r', encoding='utf-8', errors='ignore') as f:
    #     for line in f:
    #         l = line.rstrip().split('->',1)
    #         if(len(l)>1) and l[1] in count_final:
    #             count_final[l[1]] = l[0]


    # #saving the most influenced edge for each node:
    # edge = {}
    # for item in edge_count:
    #   node_end = item.split('->')[1]
    #   node_start = item.split('->')[0]
    #   if node_end not in edge or edge_count[item]>edge_count[edge[node_end]+'->'+node_end]:
    #       edge[node_end] = node_start

    # for node in count_final:
    #   count_final[node] = edge[node]

    # fr.close()
    fr = open(docdes, 'w')
    fr.write('strict digraph G{\n')
    # for i in count_final:
    #     fr.write('"'+count_final[i]+'"'+' -> '+'"'+i+'"'+'\n')
    for edge in edge_count:
        if edge_count[edge] >= 15:
            fr.write(edge+'\n')

    for i in count:
        if count[i]>=50:
            fr.write('"'+i+'"'+' [color = red]')
    fr.write('}')
    fr.close()


                    



ICmodel(network,"Enhong Chen",100)
draw_trees('./inter_res/ICres_0424.txt','./result/weighted_edge/chenehong_15.dot')
