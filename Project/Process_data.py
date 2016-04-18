from collections import defaultdict
import json
#file='SampledWebList_SmallGraph.txt'
file='./Division/sub_sampad.txt'
#file='trail.txt'
data_file= open(file, 'r')
count=0
data=[]
for line in data_file.readlines():
	line=line.split('\t')
	data.append(line)

d_word_list= defaultdict(list)

for k,	v in data:
	d_word_list[k].append(v)


d_list= defaultdict(list)

for k, v in data:
	d_list[v].append(k)

json.dump(d_word_list, open("word_list.txt",'w'))
json.dump(d_list, open("list.txt",'w'))

