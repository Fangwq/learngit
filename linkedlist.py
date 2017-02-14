# -*- coding: utf-8 -*-
import numpy as np

class Node(object):
	'''each node contains an element and the pointer 
		direct to the next element.
	'''
	def __init__(self, head, elem, pointer=None):
		self.elem = elem
		self.pointer = pointer

	def is_empty(self):
		'''check if it is empty'''
		if self.pointer is None:
			return 'the list is empty'
		else:
			return 'the lsit is not empty'

	def length(self, head):   #point is an example of class Node, and it let me think of recurrence
		'''the length of of the linked list'''
		count, node = 0, head
		while node is not None:
			count = count+1
			node = node.pointer
		return count

	def prepend(self, head, elem):
		'''insert an element in head'''
		temp = Node(elem)
		temp.pointer = head.pointer
		head = temp

	def eppend(self, end, elem):
		while end.pointer is not None:
			end = end.pointer
		end.pointer = Node(elem)

llist = Node(1)
# llist.pointer=Node(2)
# print llist.pointer
# print llist.pointer.pointer
p = llist
for i in xrange(2,11):
	p.pointer = Node(i)
	p = p.pointer
print llist.length(llist)

p=llist
while p is not None:
	print p.elem
	p=p.pointer