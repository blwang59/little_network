import codecs
import json

network = json.load(open('./inter_res/network_dict_with_conumbers.json'))

neighbors = {}


for i in network:
	neighbors[i] = set(network[i].keys())

def merge(author):

	authors_merged = set()
	authors_merged.add(author)

	author_name = author.split(':',1)[0]
	# author_aff = author.split(':',1)[1]
	flag = 1

	# print(author_name)

	while flag == 1: 
		for item in network.keys():
			item_list = item.split(':',1)
		# aff = item_list[1]

			if item_list[0]==author_name and item != author:
			
				# print('1')

				# print('author:'+author+' '+'item:'+item)
				flag = 0
				common_neighbors = len(neighbors[author] & neighbors[item])
				# print(neighbors[author])
				# print(neighbors[item])
				# print(common_neighbors)
				
				if float(common_neighbors)/float(len(neighbors[author])) >= 0.3 or float(common_neighbors)/float(len(neighbors[item])) >= 0.3:
					# print ('0')
					authors_merged.add(item)
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
print(merge('Hui Xiong:Rutgers University, Newark, NJ, USA'))

# print('end')
# print(str(merge('Enhong Chen:University of Science and Technology of China')))

def find_neighbors(root):
	for roots in merge(root):
		
	for neighbors in network[root]:
		merge(neighbors)
