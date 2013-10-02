'''
Created on 20/mag/2013

@author: raidenfox
'''

import random
from time import time
import operator

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
    B = A[:]
    
    size = len(A)
    t0 = time()
    val = randomized_select(B,0,size-1,size-i+1)
    t1 = time()
    if debug_int:
      print "La " + str(i) + " statistica d'ordine piu' grande e' " + str(val)
      print "Partizioni attorno la " + str(i) + " statistica d'ordine piu grande"
      print "Lower Partition"
      print B[0:size-i]
      print "Upper Partition"
      print B[size-i+1:size]
    t2 = time()
    randomized_quicksort(B,size-i+1,size-1)
    t3 = time()
    if debug_int:
      print "Upper Partition Ordinata"
      print B[size-i+1:size]
    tot_time = (t1-t0)+(t3-t2)
    if debug:
      print "Tempo di esecuzione di selezione tra "+ str(size) +" elementi:" + str((t1-t0)+(t3-t2))
      print ""
    return tot_time
  
def test_data(case):
  vect = {}
  total = 0
  for i in range(NTEST):
    total = total+ base + increment*(i+1)
    if case == 1 or case == 2:
      A = random_array(total)
    else:
      A = [NTEST]*total
    vect[total] = 0
    for j in range(NTEST):
      size = len(A)
      time = 0
      if case == 1:
	vect[total] = vect[total] + test(A,size/2)
      else:
	vect[total] = vect[total] + test(A,size)
    vect[total] = vect[total]/NTEST
  
  ordered = sorted(vect.iteritems(), key=operator.itemgetter(0))
  return ordered
	
def menu():
  if debug == 0:
    print "ATTENZIONE! DEBUG MODE NON ATTIVO"
  else:    
   print "## INTERACTIVE MODE ##"
   print "Seleziona il caso da lanciare in esecuzione"
   print "1 - Caso migliore"
   print "2 - Caso medio"
   print "3 - Caso peggiore"
   print "4 - Modalita' manuale"
   x = input("> ")
   
   if x == 1 or x == 2:
      print "Avvio dei test..."
      data = test_data(x)
      dataIO(data,x)
   elif x == 3:
      print "Avvio dei test..."
      data = test_data(x)
      dataIO(data,x)      
   elif x == 4:
      load_int()
   else:
      return 0
    
def dataIO(data,x):
  if x == 1:
    out_file = open("tempi_CM.txt","w")
  elif x == 2:
    out_file = open("tempi_MC.txt","w")
  elif x == 3:
    out_file = open("tempi_WC.txt","w")
    
  content = "x = [ "
  for key,value in data:
    content = content + str(key) + " "
  content = content + "]\n"
    
  content = content + "y = [ "
  for key,value in data:
    content = content + str(value) + " "
  content = content + "]"
  out_file.write(str(content))
  out_file.close()

def load_int():
  size = input("Inserisci la cardinalita': ")
  A = random_array(size)
  stat = input("Inserisci la k-sima statistica d'ordine da trovare: ")
  test(A,stat)

# Environment Params
debug = 1
debug_int = 0

# Test params
NTEST = 10
base = 1000
increment = 500

menu()

