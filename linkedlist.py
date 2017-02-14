# -*- coding: utf-8 -*-
import numpy as np

class Node(object):
	'''each node contains an element and the pointer 
		direct to the next element.
	'''
	def __init__(self, elem, pointer = None):
		self.elem = elem
		self.pointer = pointer

	def length(self, point):   #point is an example of class Node, and it let me think of recurrence
		'''the length of of the linked list'''
		count, node = 0, point
		while node is not None:
			count = count+1
			node = node.pointer
		return count

class linkedlist(Node):
	def __init__(self, header = None):
		self._header = header

	def is_empty(self):
		'''check if it is empty'''
		if self._head is None:
			return 'the list is empty'
		else:
			return 'the lsit is not empty'

	def prepend(self, elem):
		'''insert an element in the head'''
		self._header = Node(elem)

	def eppend(self, end, elem):
		'''eppend an element in the end'''
		while end.pointer is not None:
			end = end.pointer
		end.pointer = Node(elem)

	def pop(self, elem):
		if 

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