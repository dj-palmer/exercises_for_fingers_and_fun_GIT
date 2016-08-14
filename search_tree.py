#!/usr/bin/python

import pdb

""" Implementation of a binary search tree """

class Node(object):
	
	def __init__(self, key, value=None, parentKey=None):

		""" Root node constructor

			@param key: a key to refer to the node by
			@param value: data to store under the node

		""" 
		self._key = key
		self._value = value
		self._leftChild = None	 # left node
		self._rightChild = None  # right node
		self._parentKey = None   # parent reference

	def insert(self, key, value=None):
		
		if key < self._key :
			if self._leftChild is None :
				self._leftChild = Node(key, value, self._key)
			else :
				self._leftChild.insert(key, value, _leftChild._key)
		
		elif key > self._key :
			if self._rightChild is None :
				self._rightChild = Node(key, value, self._key)
			else :
				self._rightChild.insert(key, value, _rightChild._key)


	def print_tree(self) :

		print ("key: " + str(self._key), "value: " + str(self._value), "parent: " + str(self._parentKey))

		if self._leftChild :
			self._leftChild.print_tree()

		if self._rightChild :
			self._rightChild.print_tree()

"""
def main():
	print("hello world")

if __name__ == "__main__":
	main()

"""