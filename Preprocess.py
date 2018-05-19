import distance
import time
import numpy as np

def distance_matrix():
	global dist
	for i in range(0,count+1):
		for j in range(0,i):
			if i!=j:
				dist[i][j]=distance.levenshtein(seq[i],seq[j])
				dist[j][i]=dist[i][j]
				values.insert(i,dist[i][j])
				print(i)
	values.sort()
	return dist
	
def preprocess():
    global count
    t=len(lines)
    for i in range(len(lines)):
        line=lines[i]
        if line[0]=='>':
            r=""
            i+=1
            line=lines[i]
            while(line[0]!='>'):
                r+=line
                i+=1
                if i < t: 
                    line=lines[i]
                else:
                    break
            count+=1
            seq[count]=r

#MAIN
"""
Stores the distance matrix in a .npy file
"""
f=open("data_amino2.txt","r").read()
h=open("edited.txt","w")
lines=f.splitlines()
seq=dict()
values=list()
count=-1
start=time.time()
preprocess()
print("Preprocessing done\t" +str(time.time()-start))
dist = np.zeros(shape=(count+1,count+1))
start=time.time()
a=distance_matrix()
print("Distance Matrix Calculation done\t" + str(time.time()-start))
np.save('distance_matrix.npy',a)