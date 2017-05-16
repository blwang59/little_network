import json
import codecs
network = json.load(open('./inter_res/network_dict_test.json'))

neighbors = {}

# authors_merged={}


authors_merged=set(network.keys())
# authors_del=set(network.keys())

# with codecs.open('./inter_res/author_with_aff.txt', 'r', encoding='utf-8', errors='ignore') as f1:
#     for line in f1:
#         items = line.rstrip().split(' ', 2)
#         authors_merged[items[2]]=items[1]


for i in network:

	neighbors[i] = set(network[i].keys())
	

# 

class authorNode(object):
	"""docstring for authorNode"""
	def __init__(self, name, aff = set()):
		super(authorNode, self).__init__()
		self.name = name
		self.aff = aff
		#aff is a set

	def is_same(self, anothernode):
		if self.name == anothernode.name and self.aff == anothernode.aff:
			return True
		else:
			return False

	def add_aff(self, affs):
		self.aff.add(affs)





# names_affs=[]
# for i in network.keys():
# 	item = i.split(':',1)
# 	names_affs.append(item)

# for i in names_affs:
# 	for j in names_affs:
# 		if i[0]==j[0] and i[1] != j[1] and i[0]+':'+i[1] in papers_author and j[0]+':'+j[1] in papers_author:
# 			common_neighbors = float(len(set(network[i[0]+':'+i[1]].keys()) & set(network[j[0]+':'+j[1]].keys())))
# 			print('detected!')
# 			if common_neighbors/float(neighbors[i[0]+':'+i[1]]) >= 0.2 or \
# 				common_neighbors/float(neighbors[j[0]+':'+j[1]]) >= 0.2:
				
# 				print('merged!')
# 				authors_merged[i[0]+':'+i[1]+';'+j[1]] = papers_author[i[0]+':'+i[1]] + papers_author[j[0]+':'+j[1]]
# 				# del papers_author[i[0]+':'+i[1]]
# 				# del papers_author[j[0]+':'+j[1]]
count = 0

# temp_authors_merged = set(network.keys())

authors_remaining = dict.fromkeys(network.keys())

flag=1

temp_authors_merged = set(network.keys())
#to tell if merge should be continued
while flag == 1:
	flag = 0
	
	print (count)
	find = False
	index = 0
	ff = 0
	for i in temp_authors_merged:
		if ff == 1 :
			break
		for j in authors_remaining:
			index += 1
			if index > 10000000:
				ff = 1
				break

			if j==i or authors_remaining[j]==1:
				pass

			
			elif i.split(':')[0] == j.split(':')[0]:
				
				common_neighbors = len(neighbors[i] & neighbors[j])
				# print('i:'+i)
				# print('j:'+j)

				if float(common_neighbors)/float(len(neighbors[i])) >= 0.3 or float(common_neighbors)/float(len(neighbors[j])) >= 0.3:
					# if i in authors_merged and j in authors_merged:
					# print('merged!')
					# count+=1
					authors_merged.add(i+';'+j.split(':')[1])

					# if ';' in set(i):
					# 	print ('yes!')
					neighbors[i+';'+j.split(':')[1]] = neighbors[i] | neighbors[j]
					
					# if i in authors_del:
					# 	authors_del.remove(i)
					# if j in authors_del:
					# 	authors_del.remove(j)

					if i in authors_remaining:
						authors_remaining[i]=1
					if j in authors_remaining:
						authors_remaining[j]=1


					if i in authors_merged:
						authors_merged.remove(i)
					if j in authors_merged:
						authors_merged.remove(j)
						
					flag = 1
					find = True
					break

		if find:
			break
	if flag ==0 : 
		break
		


		

	print(str(flag))
	count+=1
	print('turns'+str(count))

	temp_authors_merged = authors_merged
	# temp_authors_merged = authors_merged

	# authors_remaining = authors_del


print('end')


i = 1
fr = open('./inter_res/author_with_aff_merged_30.txt', 'w', encoding='utf-8')
for items in authors_merged:
    if items!=':' :
        fr.write(str(i)+' '+str(items))
        fr.write('\n')
        i += 1
# f1.write(str(papers_author.items()))
fr.close()





for i in network_dict:
    for j in network_dict[i]:
        if author_dict[j]!=0:
            network_dict[i][j] = network_dict[i][j]/float(author_dict[j])



# fr = open('./inter_res/network_final.json', 'w',encoding = 'utf-8',errors='ignore')
# json.dump(network,fr,ensure_ascii=False)
