import json
import random
## file loading
file_name="list"
file=open(file_name+'.txt')
json1_str = file.read()
elist=json.loads(json1_str)
output_file=file_name+'seed_set'
output = open(output_file+'.txt','a')
for K in range(2,5):
	t=0
	while(t<10):
		list1=random.sample(range(0,len(elist)),1)
		list1=list1[0]
		if (len(elist[elist.keys()[list1]])>K):
			sample=random.sample(elist[elist.keys()[list1]],K)
			b=sample[0]
			for index in range (1,len(sample)):
				b=b+'\t'+sample[index]
			output.write(b)
			output.write('\n')
			t=t+1
			print(t)



	
# for i in range(0,len(elist)):
# 	if (len(elist[elist.keys()[i]])>4):
# 		print(elist[elist.keys()[i]])
