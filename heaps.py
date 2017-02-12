# -*- coding: utf-8 -*-
import numpy as np

class structure_heap(object):
    def __init__(self, array, index):
        self.array=array
        self.index=index

    def siftup(self, heap, num):
        count=0
        if num==0:
            return heap
        else:
            while num != 0: 
                if num != 2:
                    if heap[num]> heap[num/2]:
                        print num
                        count=count+1
                        heap[num],heap[num/2] = heap[num/2], heap[num]
                    else:
                        break
                else:
                    print num
                    if heap[num/2]> heap[0]:
                        heap[num/2],heap[0] = heap[0], heap[num/2]
                num=num/2
        return heap,count