import codecs
import json

network = json.load(open('./inter_res/network_dict_with_conumbers.json'))

neighbors = {}


for i in network:
	neighbors[i] = set(network[i].keys())


print(len(network))

def merge(author):

	authors_merged = set()
	authors_merged.add(author)

	author_name = author.split(':',1)[0]
	# author_aff = author.split(':',1)[1]
	flag = 1
	visited ={}
	for item in network:
		visited[item] = 0

	# print(author_name)

	while flag == 1: 
		flag = 0
		for item in network.keys():
			item_list = item.split(':',1)
		# aff = item_list[1]

			if item_list[0]==author_name and item != author and author in neighbors and visited[item] == 0:
			
				
				flag = 0
				common_neighbors = len(neighbors[author] & neighbors[item])
				
				if float(common_neighbors)/float(len(neighbors[author])) >= 0.3 or float(common_neighbors)/float(len(neighbors[item])) >= 0.3:
					# print ('0')
					authors_merged.add(item)
					visited[item] = 1
					
					# print(authors_merged)

					neighbors[author+';'+item.split(':')[1]] = neighbors[author] | neighbors[item]
					author = author+';'+item.split(':')[1]
					flag = 1

	# authors_merged=author
	

	return authors_merged
		

	# print(str(flag))
	# count+=1
	# print('turns'+str(count))

	# temp_authors_merged = authors_merged
# print(merge('Hui Xiong:Rutgers University, Newark, NJ, USA'))


# print('end')
# print(str(merge('Enhong Chen:University of Science and Technology of China')))
# print(str(merge('Jiawei Han:-')))
def find_neighbors(root):
	merged_net = {}
	# for roots in merge(root):
	# 	network[roots]

	eq = {}
	for items in merge(root):
		eq[items] = root
	i=0
	index = 0
	for neighbors in network[root]:
		if i == 1 :
			break
		if neighbors in network:
			for items in network[neighbors]:

				index += 1
				if index > 2000:
					i = 1
					break
			# print(items)

				for node in merge(items):
					eq[node] = items
	print('find 2000 nodes!')

	# print(eq['Enhong Chen:-'])

	for key in network:
		if key not in eq:
			eq[key] = key
		
		merged_net[eq[key]]={}
		for name in network[key]:
			if name not in eq:
				eq[name] = name
			if eq[name] == eq[key]:
				break
			
			if eq[name] not in merged_net[eq[key]]:

				merged_net[eq[key]][eq[name]] = network[key][name]
			else :
				merged_net[eq[key]][eq[name]] += network[key][name]

	return merged_net

merged_net = find_neighbors('Hui Xiong:-')
# merged_net = find_neighbors('Enhong Chen:-')
# if 'Enhong Chen:-' in  merged_net:
# 	print ('yes')
author_dict=dict.fromkeys(merged_net,0)

for i in merged_net:
	for j in merged_net[i]:
		if i not in author_dict:
			author_dict[i] = 0
		author_dict[i] += merged_net[i][j]


for i in merged_net:
    for j in merged_net[i]:
        if j in author_dict and author_dict[j]!=0:
            merged_net[i][j] = merged_net[i][j]/float(author_dict[j])

fr = open('./inter_res/network_merged_xionghui_u.json', 'w',encoding = 'utf-8',errors='ignore')
json.dump(merged_net,fr,ensure_ascii=False)
