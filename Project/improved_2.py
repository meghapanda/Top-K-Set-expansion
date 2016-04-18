import json
import numpy as np
from skimage.filters import threshold_otsu
import math
import time
import random
import sys
from memory_profiler import memory_usage

#file loading
file=open("word_list.txt")
json1_str = file.read()
word_list=json.loads(json1_str)

file=open("list.txt")
json1_str = file.read()
elist=json.loads(json1_str)


def similarity(term1,term2):
	num=len(set(term1).intersection(set(term2)))
	den=len(set(term1).union(set(term2)))
	sim_score=float(num)/float(den)
	return sim_score


def relevance(set1,set2):
	len_set1=len(set1)
	len_set2=len(set2)
	score_temp=0
	for i in range(0,len_set1):
		for j in range(0,len_set2):
			score_temp=score_temp+similarity(word_list[set1[i]],word_list[set2[j]])
	rel_score=score_temp/(len_set1*len_set1)
	
	return rel_score

	

# def get_K(seed_set):
# 	rel_score=[]
# 	for index in range(0,len(word_list.keys())):
# 		rel_score.append(relevance(seed_set,[word_list.keys()[index]])) 
# 	rel_score_temp=np.array(rel_score).round(2)
# 	Threshold = threshold_otsu(rel_score_temp)
# 	Threshold=round(Threshold,2)
# 	K=sum(rel_score_temp>=Threshold)
# 	return K

def create_data(term_set):
	data=[]
	data_term=[]
	for index in range(0,len(term_set)):
		data=set(data).union(set(word_list[term_set[index]]))
	data=list(data)
	for index in range(0,len(data)):
		data_term=set(data_term).union(set(elist[data[index]]))
	data_term=list(data_term)

	return data_term

	

def get_data(K,seed_set):
	data_new=seed_set
	len_data=len(data_new)
	while K>len(data_new):
		len_data=len(data_new)
		data_new=create_data(data_new)
		if (len(data_new)==len_data):
			K=len_data
			break;
	return data_new,K

# #@profile
def static_thresholding(data,seed_set,K):
	print('nodes visited',len(data))
	rel_score=[]
	R_old=[]
	R_new_temp=[]
	R_new=[]
	alpha=0.5
	for index in range(0,len(data.keys())):
		rel_score.append(relevance(seed_set,[data.keys()[index]])) 
	sorted_term_rel = np.argsort(rel_score)[::-1]
	sorted_term_rel=sorted_term_rel[0:K]

	for index in range(0,K):
		R_old.append(data.keys()[ sorted_term_rel[index]])
	
	while True:

		g_term=[]
		for index in range(0,len(data.keys())):
			sim=relevance(R_old,[data.keys()[index]])
			temp=alpha*rel_score[index]+(1-alpha)*sim
			g_term.append(temp)

		sorted_term_g = np.argsort(g_term)[::-1]
		for index in range(0,K):
			R_new.append(data.keys()[ sorted_term_g[index]])
		if (R_new!=R_old) and (set(R_new)-set(R_old))  :
			r1=(set(R_new)-set(R_old))
			r=[list(r1)[0]]
			q=R_old[-1]
			R_new_temp=(set(R_old).union(set(r)))-set(q)
			R_old=list(R_new_temp)
		else:
			R_old=R_new
			break
		
	print( 'Expanded',R_old[0:5])




def main():
    K_input=5
    K=10*K_input
    line = sys.argv[1]
    seed_set=line.rstrip()
    seed_set=seed_set.split("\t")
    print('seed set',seed_set)
    data={}
    data_temp=get_data(K,seed_set)
    K=data_temp[1]
    for i in data_temp[0]:
        data[i]=word_list[i]
    t0=time.time()
    static_thresholding(data,seed_set,K)
    t1 = time.time()
    total = t1-t0
    print('Total Time taken',total)
  
if __name__ == "__main__":
	main()
		


