#!/usr/bin/python

import pdb

""" Implementation of a binary search tree """

class Node(object):
	
	def __init__(self, key=None, value=None, parentKey=None):

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
		
		""" Just some prepopulated values to get us started """ 
		
		self.insert(10,"ten")		
		self.insert(5,"five")
		self.insert(3,"three")
		self.insert(9,"nine")
		self.insert(15,"fifteen")
		self.insert(13,"thirteen")
		self.insert(1,"one")
		self.insert(2,"two")
		self.insert(4,"four")

	def insert(self, key, value=None):
		
		""" insert a node into the tree

			@param key: a key to refer to the node by
			@param value: data to store under the node
		"""

		if self._key : 
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
			else :
				print "Failed to insert node, key already exists"
		else :  # we didn't have any root node so setup the roots key and value
			self._key = key
			self._value = value

	def getNode(self, key):

		""" returns the node object referenced by key

			@param key: key of node to return
		"""
		
		errMsg = "Sorry, can't find a node with your key"
		
		if key < self._key :
			if self._leftChild is not None :
				return self._leftChild.getNode(key)
			else :
				print errMsg
		elif key > self._key :
			if self._rightChild is not None :
				return self._rightChild.getNode(key)
			else :
				print errMsg
		elif key == self._key :
			return self
		else :
			print "Warning : Something has gone catastrophically wrong!"

	def getNodeValue(self, key):
		""" returns the data value stored under the node referenced by key 

			@param key: key of node to return
		"""

		result = self.getNode(key)._value
		print "Returning " + str(result)
		
		return result

	def setNode(self,key,value):
		""" store a value under the node referenced by key 

			@param key: key of node to return
			@param value: value to store (any data type can be stored)
		"""
		self.getNode(key)._value = value

	def print_me(self) :
		"""
			Prints out the key, values and parent key of the current node.
			Be default prints the root node.
		"""
		print ("key: " + str(self._key), "value: " + str(self._value), "parent: " + str(self._parentKey))

	def print_tree(self) :
		""" 
			Prints out the list of tree nodes and their parents.
			Ordered from smallest to largest leaves.
		"""

		if self._leftChild :
			self._leftChild.print_tree()

		self.print_me()

		if self._rightChild :
			self._rightChild.print_tree()

"""
def main():


if __name__ == "__main__":
	main()

"""