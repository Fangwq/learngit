# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from sort import algorithm_sort
import copy

# np.random.seed(1337)      #generate the same random number each time
count = 20
a0 = np.random.rand(count)*2.0-1.0 
a1 = copy.deepcopy(a0)              #As array is a mutable object, after bubblesort, it will turn into sorted array,
a2 = copy.deepcopy(a0)				#so I deepcopy the original array.
a3 = copy.deepcopy(a0)
a4 = copy.deepcopy(a0)
print 'before sorted:', a0
bubble_method = algorithm_sort(a0)
select_method = algorithm_sort(a1)
insert_method = algorithm_sort(a2)
#===calculate the time consuming===
bubble_start = time.time()
b_bubble = bubble_method.bubblesort(a0)
bubble_end = time.time()
select_start = time.time()
b_select = select_method.selectsort(a1)
select_end = time.time()
insert_start = time.time()
b_insert = insert_method.insertsort(a2)
insert_end = time.time()
print 'bubble time:', "{:.5f}s".format(bubble_end - bubble_start)
print 'select time:', "{:.5f}s".format(select_end - select_start)
print 'insert time:', "{:.5f}s".format(insert_end - insert_start)
# print 'after bubblesorted:', b_bubble
# print 'after selectsorted:', b_select
# print 'after insertsorted:', b_insert
k = np.random.randint(count)	#in case of k=0
while k == 0:					
	k = np.random.randint(count)
print 'the sampled number:',k
sample_bubble = b_bubble[0:k]
sample_select = b_select[0:k]
sample_insert = b_insert[0:k]
#=========test bottomup_merge: two nondecreasing array========
p=3;q=5;r=10
test= np.hstack([np.sort(np.random.rand(q)*2.0-1.0),np.sort(np.random.rand(r+2)*2.0-1.0)])
print test
print 'part A:', test[p-1:q]
print 'part B:', test[q:r]
merge_method = algorithm_sort(test)
result=merge_method.bottomup_merge(test,p,q,r)		#r-p+1=(q-p+1)+(r-q)
print 'merge of A and B:', result
#=========test bottomup_merge: two nondecreasing array========
print 'before sorted:', a3
bottomup_method = algorithm_sort(a3)
bottomup_start = time.time()
b_bottomup = bottomup_method.bottomupsort(a3)
bottomup_end = time.time()
print 'bottomupsort time:', "{:.5f}s".format(bottomup_end-bottomup_start)
print 'after bottomupsorted:', b_bottomup
sample_bottomup = b_bottomup[0:k]
#==========test modbinarysearch: return x's position=======
temp=np.array([2,3,6,8,9])
binary_method = algorithm_sort(temp)
index=binary_method.modbinarysearch(temp,910)
print 'the position of element x:',index
#==========test modbinarysearch: return x's position=======
print 'before sorted:', a4
modinsert_method = algorithm_sort(a4)
modinsert_start = time.time()
b_modinsert = modinsert_method.modinsertsort(a4)
modinsert_end = time.time()
print 'after bottomupsorted:', b_modinsert
print b_modinsert-b_bottomup
print 'bottomupsort time:', "{:.5f}s".format(modinsert_end-modinsert_start)
sample_modinsert = b_modinsert[0:k]
plt.figure()
plt.plot(xrange(k),sample_bubble,'ro')
plt.plot(xrange(k),sample_select,'b*')
plt.plot(xrange(k),sample_insert,'g+')
plt.plot(xrange(k),sample_bottomup,'kd')
plt.plot(xrange(k),sample_modinsert,'cx')
plt.xlim(-1,k+1)
plt.show()