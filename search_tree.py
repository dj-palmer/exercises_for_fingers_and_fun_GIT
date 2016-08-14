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
		self._leftChild = None       # left node
		self._rightChild = None	     # right node
		self._parentKey = parentKey # parent reference

	def populate(self) :
		self.insert(5,"five")
		self.insert(3,"three")
		self.insert(9,"nine")
		self.insert(15,"fifteen")
		self.insert(13,"thirteen")
		self.insert(1,"one")
		self.insert(2,"two")
		self.insert(4,"four")

	def insert(self, key, value=None):
		
		if key < self._key :
			if self._leftChild is None :
				self._leftChild = Node(key, value, self._key)
			else :
				self._leftChild.insert(key, value)
		
		elif key > self._key :
			if self._rightChild is None :
				self._rightChild = Node(key, value, self._key)
			else :
				self._rightChild.insert(key, value)


	def print_tree(self) :

		if self._leftChild :
			self._leftChild.print_tree()

		print ("key: " + str(self._key), "value: " + str(self._value), "parent: " + str(self._parentKey))

		if self._rightChild :
			self._rightChild.print_tree()

"""
def main():


if __name__ == "__main__":
	main()

"""