#!/usr/bin/python

#import pdb
from key import Key

""" Implementation of a binary search tree """

class BinaryNode(object):
	
	def __init__(self, key=None, value=None, parentKey=None):

		""" Root node constructor

			@param key: a key to refer to the node by
			@param value: data value to store under the node

		""" 
		self._key = key 
		self._value = value
		self._leftChild = None       # left node
		self._rightChild = None	     # right node
		self._parentKey = parentKey # parent reference

	def insert(self, key, value=None):
		
		""" insert a node into the tree """

		if self._key : 
			
			if key == self._key :
				print "Failed to insert node, key already exists"
			elif key < self._key :
				if self._leftChild is None :
					self._leftChild = type(self)(key, value, self._key)
				else :
					self._leftChild.insert(key, value)
			elif key > self._key :
				if self._rightChild is None :
					self._rightChild = type(self)(key, value, self._key)
				else :
					self._rightChild.insert(key, value)
			else :
				print "Warning : Something has gone catastrophically wrong!"
		
		else :  # we didn't have any root node so setup the roots key and value
			self._key = key
			self._value = value

	def getNode(self, key):

		""" returns the node object referenced by key """
		
		errMsg = "Sorry, can't find a node with your key"
		
		if key == self._key :
			return self
		elif key < self._key :
			if self._leftChild is not None :
				return self._leftChild.getNode(key)
			else :
				print errMsg
				return None
		elif key > self._key :
			if self._rightChild is not None :
				return self._rightChild.getNode(key)
			else :
				print errMsg
				return None
		else :
			print "Warning : Something has gone catastrophically wrong!"

	def getNodeValue(self, key):
		""" returns the data value stored under the node referenced by key """

		try :
			result = self.getNode(key)._value
		
			print "Returning " + str(result)
			return result

		except AttributeError :
			return None

	def setNode(self,key,value):
		""" store a value under the node referenced by key """
		
		try :
			self.getNode(key)._value = value

		except AttributeError :
			return None

	def print_me(self):
		"""
			Prints out the key, values and parent key of the current node.
			By default prints the root node.
		"""
		print ("key: " + str(self._key), "value: " + str(self._value), "parent: " + str(self._parentKey))

	def print_tree(self):
		""" 
			Prints out the list of tree nodes and their parents.
			Ordered from smallest to largest leaves.
		"""

		if self._leftChild :
			self._leftChild.print_tree()

		self.print_me()

		if self._rightChild :
			self._rightChild.print_tree()

class TernaryNode(BinaryNode):
	
	""" Extends the BinaryNode class so a node can have up to 3 children """

	def __init__(self, key=None, value=None, parentKey=None):
		BinaryNode.__init__(self, key, value, parentKey)
		self._midChild = None

	def insert(self, key, value=None):

		# An extension to the binary tree insert method.
		# If we haven't got a left and right child proceed as usual.
		# But if we do, check if the key is between those values, and if it is, populate the middle child

		if self._key :

			if key == self._key :
				print "Failed to insert node, key already exists"
			elif (self._leftChild is None) or (self._rightChild is None) : # we haven't yet populated 2 keys of the node yet so treat as binary
				BinaryNode.insert(self, key, value)
			# now we must have left and right children
			elif key < self._leftChild._key : 
				self._leftChild.insert(key, value)
			elif key > self._rightChild._key :
				self._rightChild.insert(key, value)
			# we're between our children to make or descend the middle child
			elif (key > self._leftChild._key) and (key < self._rightChild._key) :
				if self._midChild is None :
					self._midChild = TernaryNode(key, value, self._key)
				else :
					self._midChild.insert(key, value)
			else : 
				print "Warning : Something has gone catastrophically wrong!"

		else :
			BinaryNode.insert(self, key, value)

	def getNode(self, key):

		# An extension to the binary tree get method.
		# If we have a middle child and the key we are searching for is between us, descend the middle child.
		# Otherwise we know we can just follow the binary search method.
		
		if key == self._key :
			return self
		elif self._midChild and (key > self._leftChild._key) and (key < self._rightChild._key) :
				return self._midChild.getNode(key)
		else : 
			return BinaryNode.getNode(self, key)

	def print_tree(self):
		
		if self._leftChild :
			self._leftChild.print_tree()

		if self._midChild :
			if self._midChild._key < self._key :
				self._midChild.print_tree()

		self.print_me()
		
		if self._midChild :
			if self._midChild._key > self._key :
				self._midChild.print_tree()
			
		if self._rightChild :
			self._rightChild.print_tree()


def main():

	print "----------------------------------------------------- "
	print " We're going to create a search tree inserting the    "
	print " following keys in order :                            "
	print " 10, 5, 3, 9, 15, 13, 1 ,2, 4, 100                    "
	print "----------------------------------------------------- "
	print ""
	
	print "----------------------------------------------------- "
	print "Creating a binary search tree with these integer keys "
	print "----------------------------------------------------- "

	tree1 = BinaryNode()
		
	tree1.insert(10,"ten")		
	tree1.insert(5,"five")
	tree1.insert(3,"three")
	tree1.insert(9,"nine")
	tree1.insert(15,"fifteen")
	tree1.insert(13,"thirteen")
	tree1.insert(1,"one")
	tree1.insert(2,"two")
	tree1.insert(4,"four")
	tree1.insert(100, "hundred")

	print " Your tree now looks like (smallest to largest): "
	tree1.print_tree()
	print "\n Inserting key,value (14, \"fourteen\") : "
	tree1.insert(14,"fourteen")
	print " Your tree now looks like (smallest to largest): "
	tree1.print_tree()
	print "\n Updating value for key 14 to \"newfourteen\" "
	tree1.setNode(14,"newfourteen")
	print " Your tree now looks like (smallest to largest): "
	tree1.print_tree()
	
	print "----------------------------------------------------- "
	print "Creating a binary search tree with keys as words      "
	print "----------------------------------------------------- "
	print "Bit of a random example..."
	print "Creating a binary search tree with the key defined as the number of letters in the number \n"

	tree2 = BinaryNode()

	tree2.insert(Key("ten"),"ten")		
	tree2.insert(Key("five"),"five")
	tree2.insert(Key("three"),"three")
	tree2.insert(Key("nine"),"nine")
	tree2.insert(Key("fifteen"),"fifteen")
	tree2.insert(Key("thirteen"),"thirteen")
	tree2.insert(Key("one"),"one")
	tree2.insert(Key("two"),"two")
	tree2.insert(Key("four"),"four")	
	tree2.insert(Key("hundred"), "hundred")

	print " Your tree now looks like (smallest to largest): "
	tree2.print_tree()
	print "\n Inserting key,value (Key(\"eleven\"), \"neweleven\") : "
	tree2.insert(Key("eleven"),"eleven")
	print " Your tree now looks like (smallest to largest): "
	tree2.print_tree()
	print "\n Updating value for key \"eleven\" to \"neweleven\" "
	#pdb.set_trace()
	tree2.setNode(Key("eleven"),"neweleven")
	print " Your tree now looks like (smallest to largest): "
	tree2.print_tree()

	print "----------------------------------------------------- "
	print "Creating a search tree with ternary nodes             "
	print "----------------------------------------------------- "
	
	tree3 = TernaryNode()

	tree3.insert(10,"ten")		
	tree3.insert(5,"five")
	tree3.insert(3,"three")
	tree3.insert(9,"nine")
	tree3.insert(15,"fifteen")
	tree3.insert(13,"thirteen")
	tree3.insert(1,"one")
	tree3.insert(2,"two")
	tree3.insert(4,"four")
	tree3.insert(100, "hundred")

	print "Your tree now looks like (smallest to largest): "
	tree3.print_tree()
	print "\n Inserting key,value (14, \"fourteen\") : "
	tree3.insert(14,"fourteen")
	print " Your tree now looks like (smallest to largest): "
	tree3.print_tree()
	print "\n Updating value for key 14 to \"newfourteen\" "
	tree3.setNode(14,"newfourteen")
	print " Your tree now looks like (smallest to largest): "
	tree3.print_tree()

	print "------------------------------------------------"

if __name__ == "__main__":
	main()
