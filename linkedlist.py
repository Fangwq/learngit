# -*- coding: utf-8 -*-
import numpy as np
import random
#conclusion: the most important thing in the linked list structure 
#is the head, and it is a little like recurrence
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
		while p.pointer is not None:
			p = p.pointer
		p.pointer = Node(elem)   #p.pointer.pointer = None

	def pop(self):        #pop the first element
		if self._header is None:
			print "the list is empty"
		e = self._header.elem
		self._header = self._header.pointer
		return e

	def pop_last(self):
		if self._header is None:
			print "the list is empty"
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

	# def find(self, pred):    
	# 	'''find the element which is equal to value pred'''
	# 	p = self._header
	# 	count = 0
	# 	while p is not None and pred != p.elem:
	# 		count = count+1
	# 		p = p.pointer
	# 	if count == self._header.length(self._header):
	# 		return 'the element you find is not in the list'
	# 	return count
	
	# use find function, I can pop any one
	def find(self, index):    
		'''find the element with its index'''
		if type(index) != int:
			raise Exception('the value index must be integer')
		p = self._header
		count = 0
		while p is not None and index != count:
			count = count+1
			p = p.pointer
		if p is not None:
			x = p.elem
			return x,'**'
		else:
			return 'the index is out of length'

	def print_all(self):
		p = self._header
		while p is not None:
			print p.elem,'',   #,not line break
			p = p.pointer
		print ''

	def reverse(self):
		p = self._header
		if p is None or p.pointer is None:
			return
		p = None
		while self._header is not None:
			q = self._header 
			self._header = q.pointer
			q.pointer = p
			p = q
		self._header = p

	def sort(self):
		p = self._header
		if p is None and p.pointer is None:
			return
		rem = p.pointer
		p.pointer = None
		while rem:
			p = self._header
			q = None
			while p and p.elem <= rem.elem:
				q = p
				p = p.pointer
			if q is None:
				self._header = rem
			else:
				q.pointer = rem
			q = rem
			rem = rem.pointer
			q.pointer = p

	# def elements(self):
	# 	p = self._header
	# 	while p:
	# 		yield p.elem
	# 		p = p.pointer

llist = Node(1)
p = llist
for i in xrange(2,11):
	p.pointer = Node(i)
	p = p.pointer
print llist.length(llist)

p=llist
while p is not None:
	print p.elem
	p=p.pointer

mlist1 = linkedlist()
# print mlist1.random_pop(1)
for i in range(10):
    mlist1.prepend(i)

for i in range(11, 20):
    mlist1.endpend(i)

mlist1.print_all()
for i in range(5):
    print mlist1.pop()
    print mlist1.pop_last()

# print 
print mlist1.find(8)
print 'remained:'
mlist1.print_all()
mlist1.reverse()
print 'reversed:'
mlist1.print_all()
# mlist1.sort()
# mlist1.print_all()
# for x in mlist1.elements():
#     print x
# print '\n'
