'''
Created on 20/mag/2013

@author: raidenfox
'''

import random
from time import time

def partition(A,p,r):
    x = A[r]
    i = p-1
    j = p
    while j < r:
        if A[j] <= x:
            i = i+1
            k = A[j]
            A[j] = A[i]
            A[i] = k
        j = j+1
    h = A[i+1]
    A[i+1] = A[r]
    A[r] = h
    return i+1

def randomized_partition(A,p,r):
    q = random.randint(p,r)
    k = A[q]
    A[q] = A[r]
    A[r] = k
    return partition(A,p,r)
  
def randomized_quicksort(A,p,r):
    if p < r:
      q = randomized_partition(A,p,r)
      randomized_quicksort(A,p,q-1)
      randomized_quicksort(A,q+1,r)
      
def mod_partition(A,pos):
    q = position_arr(A,pos)
    # Scambio di posizioni
    k = A[len(A)-1]
    A[len(A)-1] = A[q]
    A[q] = k
    return partition(A,0,len(A)-1)

def randomized_select(A,p,r,i):
    if p==r:
        return A[p]
    
    q = randomized_partition(A,p,r)
    k = q-p+1
    
    if i == k:
        return A[q]
    else:
        if i < k:
            return randomized_select(A,p,q-1,i)
        else:
            return randomized_select(A,q+1,r,i-k)

def position_arr(A,val):
    return A.index(val)

def random_array(size):
    return random.sample(range(size),size)
        
def test(A,i):
    #print A
    B = A[:]
    
    size = len(A)
    t0 = time()
    val = randomized_select(B,0,size-1,size-i+1)
    t1 = time()
    #print "La " + str(i) + " statistica d'ordine piu' grande e' " + str(val)
    #print B
    t2 = time()
    randomized_quicksort(B,size-i+1,size-1)
    t3 = time()
    #print "Array ordinato"
    tot_time = (t1-t0)+(t3-t2)
    print "Tempo di esecuzione di "+ str(size) +" elementi:" + str((t1-t0)+(t3-t2))
    print ""
    return tot_time
  
def main():
    out_file = open("tempi2.txt","w")

    vect = [0]*10
    increment = 5000
    for j in range(10):
      total = 0
      for i in range(10):
	total = total + increment*(i+1)
	A = random_array(total)
	tm = test(A,len(A))
	vect[i] = vect[i] + tm
	
    for k in range(10):
      vect[k] = vect[k]/10
      
    out_file.write(str(vect))
    out_file.close()
    print vect

main()