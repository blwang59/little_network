import json
import codecs
network = json.load(open('./network_dict_test.json'))
papers_per_author = {}
with codecs.open('./author_with_aff.txt', 'r', encoding='utf-8', errors='ignore') as f1:
    for line in f1:
        items = line.rstrip().split(' ', 2)
        papers_per_author[items[0]] = items[1]

for i in network:
	for j in network[i]:
		network[i][j] = network[i][j]/int(papers_per_author[j])


fr = open('./network_final.json', 'w',encoding = 'utf-8',errors='ignore')
json.dump(network,fr,ensure_ascii=False)
