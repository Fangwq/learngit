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

class linkedlist(object):
	def __init__(self):
		# super(linkedlist,self).__init__()
		self._header = None

	def is_empty(self):
		'''check if it is empty'''
		if self._header is None:
			return 'the list is empty'
		else:
			return 'the list is not empty'

	def prepend(self, elem):
		'''append an element in the head'''
		self._header = Node(elem, self._header)

	def endpend(self, elem):
		'''append an element in the end'''
		if self._header is None:
			self._header = Node(elem)
			return
		p = self._header
		while p is not None:
			p = p.pointer
		p.pointer = Node(elem)   #p.pointer.pointer = None

	def pop(self):
		if self._header is None:
			raise Exception("the list is empty")
		e = self._header.elem
		self._header = self._header.pointer
		return e

	def pop_last(self):
		if self._header is None:
			raise Exception("the list is empty")
		p = self._header
		if p.pointer is None:  #If only one element
			e = p.elem
			self._header=None
			return e
		while p.pointer.pointer is not None:    #find the last
			p = p.pointer
		e = p.pointer.elem
		p.pointer = None
		return e

	def find(self, pred):
		p = self._header
		count = 0
		while pred != p.elem and p is not None:
			count = count+1
			p = p.pointer
		if count==self._header.length(self._header)-1:
			print 'the pred is not in the list'
		return count

	def print_all(self):
		p = self._header
		while p is not None:
			print p.elem,', ',   #, for not line break
			p = p.pointer
		print ''





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