#!/usr/bin/python

#==============
#Grouping sheep
#==============
# 
# Setup:
#   Order the co-ordinates of your sheep.
#   Specify a start point to start grouping from (or assume start point is centre of the field).
#
# Algorithm: 
#   To group the sheep into pens P(i) of size x by y
#			1. From the start point, group sheep within x/2 horizontal and y/2 vertical distance - pen P(1). 
# 			2. Get the next sheep S in your ordered list... that has not been grouped, but is closest to the centre of the current pen P(i). Sheep S will sit in the next pen P(i+1)
#			3. Identify if sheep S is above, below, to left or to right of Pen P(i).
#			4. Try grouping in vicinity of S based on direction of S from Pen(i) and select group that maximises number of sheep
#				e.g. If S above Pen(i), find sheep max y distance above S, but within x/2 to the left/right of S. Group G(above)
#				     If S below Pen(i), find sheep max y distance below S, but within x/2 to the left/right of S. Group G(below)
#				     If S to the right of Pen(i), find sheep max x distance to the right of S, within y/2 above/below S. Group G(right)
#					 If S to the left of Pen(i), find sheep max x distance to the left of S, within y/2 above/below S. Group G(left)
#				Pen(i+1) = max {Group(above), Group(below), Group(left), Group(right).
#			5.  Repeat from step 2 until all sheep have been captured.
#			6.  Finally count the number of pens we have.
#			
# As an extension, but not completed here, could iterate through different pen sizes to find the range of groupings	 

# Things to consider where things go wrong!
#	- When getting next sheep S there may be ones equidistant from the centre of the current Pen. Will need a way to chose which to select.
#   - There may be no sheep in Pen(1), so we need a way of discounting this pen. 
#   - Sheep could move!

# Advantages
# 	- Attempts to group sheep by proximity to each other. I think this is most natural way of thinking of grouping sheep,
#     although there are of course alternatives -- e.g. could use concentric pens.
#   - Efficiency gained by not checking back for sheep in the direction we came from -- since otherwise we would have
#     have encountered that sheep before reaching sheep S. But per disadvantages this does run risk of missing nearby sheep.

# Disadvantages
# 	- Some inefficiency in the groupings - possibility that a pen could cross over with a previous pen
#	  (tried to minimise this through the use of grouping based on direction from previous pen)
#   - However, by using direction from previous, risk of missing other nearby sheep in opposite direction.
#   - If start point is specified at the edge of a field, already 
#   - Does not account for sheep in 3D! 

import pdb

class Flock(object):
	
	sheep = [(1,1),(2,3),(5,6),(6,6),(2,2)]
	ordered_sheep = sheep.sort

	def __init__(self, centre_of_field=None):

		if centre_of_field is not None :
			self.centre_of_field = centre_of_field
	

def main():

	flock = Flock()
	# TBC...

if __name__ == "__main__":
	main()