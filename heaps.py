# -*- coding: utf-8 -*-
import numpy as np

class structure_heap(object):
    '''I handel the problem in heap data structure'''
    def __init__(self, array):
        self._array=array

    def siftup(self, heap, num):
        '''sift up the element whose key is greater than the key of its parent.'''
        count=0
        if num==0:
            return heap
        else:
            while num != 0:   #in this method, I don't need to consider if num is odd or even 
                if heap[num]> heap[(num-1)/2]:
                    # print num
                    count=count+1
                    heap[num], heap[(num-1)/2] = heap[(num-1)/2], heap[num]
                else:
                    break
                num=(num-1)/2
        # print count
        return heap

    def siftdown(self, heap, num):
        '''sift down the element whose key is smaller than the key of its max son.'''
        count=0
        if 2*num > len(heap):
            return heap
        else:
            while 2*num < len(heap):
                num=2*num+1
                if num+1 < len(heap) and heap[num+1] > heap[num]:
                    num=num+1
                if heap[num] > heap[(num-1)/2]:
                    # print num
                    # count=count+1
                    heap[num], heap[(num-1)/2] = heap[(num-1)/2], heap[num]
        # print count
        return heap

    def insert(self, heap, x):
        '''insert an element in a heap'''
        num=len(heap)
        heap=np.hstack([heap, x])
        self.siftup(heap,num)

        return heap

    def delete(self, heap, num):
        '''delete an element in a heap'''
        length=len(heap)
        x=heap[num]; y=heap[length-1]
        length=length-1
        if num==length:
            # print '===='
            return heap[0:length]
        heap[num]=y
        if y > x:
            self.siftup(heap, num)
        else:
            self.siftdown(heap, num)
        return heap[0:length]

    def make_heap(self, heap):
        '''turn an array into heap'''
        heap=self._array
        length=len(heap)
        for i in xrange((length-1)/2,-1,-1):
            self.siftdown(heap, i)
        return heap

