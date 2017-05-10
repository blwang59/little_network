import json
import codecs
network = json.load(open('./inter_res/network_dict_test.json'))

datas = {}
for i in set(network.keys()):
	for j in set(network.keys()):
		if i!=j and i.split(':')[0] == j.split(':')[0]:
			if i.split(':')[0] not in datas:
				datas[i.split(':')[0]] = set()
				datas[i.split(':')[0]].add(i)
				datas[i.split(':')[0]].add(j)
			else:
				datas[i.split(':')[0]].add(i)
				datas[i.split(':')[0]].add(j)
			

print(datas.items())
# for i in network:
# 	neighbors[i] = set(network[i].keys())


# for name in datas:

# 	for i in datas[name]:
# 		for j in datas[name]:
# 			common_neighbors = len(neighbors[i] & neighbors[j])
		
# 				if float(common_neighbors)/float(len(neighbors[i])) >= 0.3 or float(common_neighbors)/float(len(neighbors[j])) >= 0.3:
					
# 					authors_merged.add(i+';'+j.split(':')[1])
	
# 					neighbors[i+';'+j.split(':')[1]] = neighbors[i] | neighbors[j]