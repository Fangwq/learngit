# -*- coding: utf-8 -*-
import numpy as np

def find(x):
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]

def rank(x):
	count = 1
	while parent[x] != x:
		count = count+1
		x = parent[x]
	return count

def union(x, y):
	x_root = find(x)
	y_root = find(y)
	if x_root == y_root:   #in same set
		break
	if rank[x_root] > rank[y_root]:
		parent[y_root] = x_root
		if rank[x_root] == rank[y_root]:
			rank[y_root] = rank[y_root] + 1
	else:
		parent[x_root] = y_root
	return x+y


#this method need to know the node and its parent. In function find, 
#the recursion line realize the path compression process. The rank can be 
#known from the count of searching parent. And rank heuristic is used in union.