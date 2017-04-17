import codecs
mess = {}
papers_per_author = {}
pc = 0
author_list = []
size=0
sizeo=0
with codecs.open('./AMiner-Paper.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if line != '\n':
            line1 = line.rstrip().split(' ', 1)
            if len(line1) <= 1 :
                continue
            line2 = line1[1].split(';')
            for i in range(0, len(line2)):
                mess[line1[0]+str(i)] = line2[i]

        if line[:2] == '#@':
            size = len(line[3:-1].split(';'))
        if line[:2] == '#o':
            sizeo = len(line[3:-1].split(';'))
        if line == '\n':

            for i in range(0, min(size,sizeo)):
                if mess['#@'+str(i)]+':'+mess['#o'+str(i)] not in papers_per_author:

                    papers_per_author[mess['#@'+str(i)]+':'+mess['#o'+str(i)]] = 1
                else:
                    papers_per_author[mess['#@' + str(i)] + ':' + mess['#o' + str(i)]] += 1
            mess = {}

            size = 0
            sizeo = 0


       # print(papers_per_author.items())
i = 1
f1 = open('./author_with_aff.txt', 'w', encoding='utf-8')
for items in papers_per_author:
    if papers_per_author[items] > 5 and items!=':' :
        f1.write(str(i)+' '+str(papers_per_author[items])+' '+str(items))
        f1.write('\n')
        i += 1
# f1.write(str(papers_per_author.items()))
f1.close()
