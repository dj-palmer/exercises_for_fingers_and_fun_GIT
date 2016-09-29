# exercises_for_fingers_and_fun_GIT

Just a bit of fun! Both these files are executable to give a demo of the exercises.

**flock.py**
An implementation of an algorithm I designed to group a flock of 
sheep, given a set of coordinates for the sheep. A demo of
parametising as much as possible to keep the solution super
flexible.

Given a point to start, it begins by finding the nearest sheep, 
then tries to 'pen' as many sheep within a specified radius.
From there it tries to find the closest sheep not penned and
continue, resulting in an array of the pens and details of the
grouped sheep.

**search_tree.py**
My implementation a ternary search tree... whilst trying to
demonstrate a couple of OOP/python features. For one, inheritance...
The ternary tree extends a basic binary tree. The next is 
abstract classes... using this to force implementation of 
comparators for traversing the tree.
(Just an exercise -- thought this a bit more interesting than
the usual comparator methods)
