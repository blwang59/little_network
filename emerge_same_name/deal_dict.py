import json
import codecs
network = json.load(open('./inter_res/network_dict_test.json'))

neighbors = {}

# authors_merged={}


authors_merged=set()
authors_del=set(network.keys())

# with codecs.open('./inter_res/author_with_aff.txt', 'r', encoding='utf-8', errors='ignore') as f1:
#     for line in f1:
#         items = line.rstrip().split(' ', 2)
#         authors_merged[items[2]]=items[1]


for i in network:

	neighbors[i] = set(network[i].keys())
	

# 


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

temp_authors_merged = set(network.keys())

temp_del_authors = set(network.keys())


flag=1#to tell if merge should be continued
while flag == 1:


	for i in temp_authors_merged:

		for j in temp_del_authors:

			if j==i:
				pass

			
			elif i.split(':')[0] == j.split(':')[0]:
				
				common_neighbors = len(neighbors[i] & neighbors[j])
				# print('i:'+i)
				# print('j:'+j)

				if float(common_neighbors)/float(len(neighbors[i])) >=0.3 or float(common_neighbors)/float(len(neighbors[j])) >=0.3:
					# if i in authors_merged and j in authors_merged:
					# print('merged!')
					# count+=1
					authors_merged.add(i+';'+j.split(':')[1]) 
					neighbors[i+';'+j.split(':')[1]] = neighbors[i] | (neighbors[j])
					
					if i in authors_del:
						authors_del.remove(i)
					if j in authors_del:
						authors_del.remove(j)

					
					
					flag = 1
				else:
					flag = 0

					# print(i+';'+j.split(':')[1])

	# print(count)
	temp_authors_merged = authors_merged

	temp_del_authors = authors_del


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





	



# fr = open('./inter_res/network_final.json', 'w',encoding = 'utf-8',errors='ignore')
# json.dump(network,fr,ensure_ascii=False)
