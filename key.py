#!/usr/bin/python

from abc import ABCMeta, abstractmethod

class AbstractKey(object):
	"""
		an abstract base class for a key comparator.
		Allows for an implementation of ==,<,> comparators for choosing which
		nodes to descend in the search_tree module
	"""  
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def __eq__(self, other):
		""" allow for custom defintion of equals comparator"""
		pass

	@abstractmethod
	def __gt__(self, other):
		""" allow for custom defintion of greater than comparator"""
		pass

	@abstractmethod
	def __lt__(self, other):
		""" allow for custom defintion of less than comparator"""
		pass

class Key(AbstractKey):
	""" 
		a simple example of an implementation of key comparison to choose
		how to traverse the tree -- based on length of key name
	"""

	def __init__(self, name):
		# define your key properties here
		self._name = str(name);

	def __eq__(self, other):
		# define your equals comparator here
		return not len(self._name) > len(other._name) and not len(self._name) < len(other._name)

	def __gt__(self, other):
		# define your greater than comparator here
		return len(self._name) > len(other._name)
	
	def __lt__(self, other):
		# define your less than comparator here
		return len(self._name) < len(other._name)

