# -*- coding: utf-8 -*-
import numpy as np

class structure_heap(object):
    '''I handel the problem in heap data structure'''
    def __init__(self, array, index):
        self.array=array
        self.index=index

    def siftup(self, heap, num):
        count=0
        if num==0:
            return heap
        else:
            while num != 0:   #in this method, I don't need to consider if num is  the odd or even 
                if heap[num]> heap[(num-1)/2]:
                    print num
                    count=count+1
                    heap[num], heap[(num-1)/2] = heap[(num-1)/2], heap[num]
                else:
                    break
                num=(num-1)/2
        # print count
        return heap