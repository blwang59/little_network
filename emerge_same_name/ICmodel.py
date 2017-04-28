import json
import random

network = json.load(open('./inter_res/network_final.json'))


def ICmodel(net,seeds,times):

	net=network
	fr = open('./inter_res/ICres.txt', 'w', encoding='utf-8')
	for i in range(times):
		target = []
		active = set()
		# status = {}
		edges = {}
	# for i in net:
	# 	for j in net[i]:

	#neighbor_dict = net[seeds]
	#neighbor_q = neighbor_dict.keys()
		#fr = open('./ICres.txt', 'w', encoding='utf-8')
		target.append(seeds)
		active.add(seeds)
		ltimes = 0
		while(target):
			ltimes+=1
			node = target.pop(0)

			# active.add(node)
			# status[node]=1
			for follower in net[node]:
				if follower not in active :
					if random.random() <= net[node][follower]:
						target.append(follower)
						active.add(follower)
						# status[follower]=1

					    	# edges[node + '->' + follower]=1



						fr.write(node + ' ' + follower + ' '+str(ltimes)+'\n')

		fr.write('\n')

	fr.close()



ICmodel(network,"4688",100)







