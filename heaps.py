# -*- coding: utf-8 -*-
import numpy as np

class structure_heap(object):
    '''I handel the problem in heap data structure'''
    def __init__(self, array):
        self._array=array
        self._len=len(array)

    def siftup(self, heap, num):
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
        count=0
        if 2*num > len(heap):
            return heap
        else:
            while 2*num <= len(heap):
                num=2*num+1
                if num+1 < len(heap) and heap[num+1] > heap[num]:
                    num=num+1
                if heap[num] > heap[(num-1)/2]:
                    # print num
                    count=count+1
                    heap[num], heap[(num-1)/2] = heap[(num-1)/2], heap[num]
        # print count
        return heap