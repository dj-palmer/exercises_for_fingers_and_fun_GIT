#!/usr/bin/python

#==============
#Grouping sheep
#==============
# 
# Setup:
#   Specify a start point to start grouping from (or assume start point is centre of the field).
#
# Algorithm: 
#   To group the sheep into pens P(i) of size x by y
#           1. From the start point, group sheep within +/- x/2 horizontal and +/- y/2 vertical distance - pen P(1). 
#           2. Get the next sheep S in your list that has not been grouped, but is closest to the centre of the current pen P(i). Sheep S will sit in the next pen P(i+1)
#           3. Identify if sheep S is above, below, to left or to right of Pen P(i).
#           4. Try grouping in vicinity of S based on direction of S from Pen(i) and select group that maximises number of sheep
#               e.g. If S above Pen(i), find sheep max y distance above S, but within x/2 to the left/right of S. Group G(above)
#                    If S below Pen(i), find sheep max y distance below S, but within x/2 to the left/right of S. Group G(below)
#                    If S to the right of Pen(i), find sheep max x distance to the right of S, within y/2 above/below S. Group G(right)
#                    If S to the left of Pen(i), find sheep max x distance to the left of S, within y/2 above/below S. Group G(left)
#               Pen(i+1) = max {Group(above), Group(below), Group(left), Group(right).
#           5.  Repeat from step 2 until all sheep have been captured.
#           6.  Finally count the number of pens we have.
#           
# As an extension, but not completed here, could iterate through different pen sizes to find the range of groupings  

# Things to consider where things go wrong!
#   - When getting next sheep S there may be ones equidistant from the centre of the current Pen. Will need a way to chose which to select.
#     Currently just selects the first sheep we come to.
#   - When looking at max number of elements in the Group we may have same size groups, need to handle.
#   - Sheep could be on the cusp of a pen - important not to miss / double-count
#   - There may be no sheep in Pen(1), so we need a way of discounting this pen. 
#   - Sheep could move!

# Advantages
#   - Attempts to group sheep by proximity to each other. I think this is most natural way of thinking of grouping sheep,
#     although there are of course alternatives -- e.g. could use concentric pens.
#   - Efficiency gained by not checking back for sheep in the direction we came from -- since otherwise we would have
#     have encountered that sheep before reaching sheep S. But per disadvantages this does run risk of missing some nearby sheep.

# Disadvantages
#   - Some inefficiency in the groupings - possibility that a pen could cross over with a previous pen
#     (tried to minimise this through the use of grouping based on direction from previous pen)
#   - However, by using direction from previous, risk of missing other nearby sheep in opposite direction.
#   - If start point is specified at the edge of a field, already introduced inefficiency of grouping
#   - Does not account for sheep in 3D! 
#   - Inefficient -- completes in time proportional to size of array

# import pdb


class Flock(object):

    def __init__(self, start_point=None, pen_size=(1,1)):

        # Define your sheep here!
        self.sheep = [(-0.1,-0.1),(-1,-1),(1,1),(2,3),(4.9,5.9),(5,6),(6,6),(2,2)]

        if start_point is not None :
            self.start_point = start_point
        else : 
            self.start_point = ( (max(self.sheep)[0] + min(self.sheep)[0]) / 2.0 , (max(self.sheep)[1] + min(self.sheep)[1]) / 2.0 )
    
        self.pen_size = pen_size

def main():
    
    start_point = (0,0) 
    pen_size = (3,3)
    flock = Flock(start_point, pen_size)
    
    print "------------------------------------------- "
    print " Grouping Algorithm for a Flock of Sheep    "
    print "------------------------------------------- "
    
    print " Our sheeps co-ordinates : "
    print flock.sheep
    
    print " \n Grouping starting nearby %s and with pen size %s by %s " % (start_point, pen_size[0], pen_size[1])
    group_sheep(flock, start_point, pen_size)

    # now try at centre of field
    flock = Flock(pen_size=pen_size)
    start_point = flock.start_point
    
    print " \n Grouping starting at centre of field %s and with pen size %s by %s " % (start_point, pen_size[0], pen_size[1])
    group_sheep(flock, start_point, pen_size)
    
    # Repeat above but with different pen_size
    pen_size = (1,3)
    start_point = (0,0) 
    flock = Flock(start_point, pen_size)
    print " \n Grouping starting nearby %s and with pen size %s by %s " % (start_point, pen_size[0], pen_size[1])
    group_sheep(flock, start_point, pen_size)
    
    flock = Flock(pen_size=pen_size)
    start_point = flock.start_point

    print " \n Grouping starting at centre of field %s and with pen size %s by %s " % (start_point, pen_size[0], pen_size[1])
    group_sheep(flock, start_point, pen_size)
    
def distance(coord1,coord2):
    return ( (abs(coord2[0]-coord1[0])**2 + abs(coord2[1]-coord1[1])**2) ** (1/(2.0)) )

def group_sheep(flock, start_point, pen_size):
    
    my_sheep = flock.sheep
    start_point = flock.start_point
    pen_distX = flock.pen_size[0]
    pen_distY = flock.pen_size[1]
    pen_distX_var = flock.pen_size[0]/2.0
    pen_distY_var = flock.pen_size[1]/2.0
    pens=[]
    cur_pen=[]
    cur_pen_num=0
    
    # First pass set the first pen
    for x,y in my_sheep :
        if ( abs(x-start_point[0]) <= pen_distX_var and abs(y-start_point[1]) <= pen_distY_var) :
            cur_pen.append((x,y))
    
    # recording the group if we found sheep
    if len(cur_pen) > 0 :
        cur_pen_num = cur_pen_num + 1
        pens.append({"Pen%s" % (cur_pen_num) : cur_pen})
        
        for sheep in cur_pen :
            my_sheep.remove(sheep)
    

    # If we haven't caught all the sheep
    while len(my_sheep) > 0 :
        
        cur_pen_num = cur_pen_num + 1
        cur_pen = []

        # initially choose next sheep available but then we'll find the closest sheep to the previous pen
        # so we can try and group around it
        next_sheep = my_sheep[0] 
        
        for x,y in my_sheep :
            if distance((x,y),start_point) < distance(next_sheep,start_point) :
                next_sheep = (x,y)

        pen_above = [next_sheep]
        pen_below = [next_sheep]
        pen_left = [next_sheep]
        pen_right = [next_sheep]

        for x,y in my_sheep :
            # try a few different groupings dependent on whether the next sheep was above, below, left or right of where we were.
            if (x,y) != next_sheep :
                if next_sheep[1] > start_point[1]:
                    if ( abs(x-next_sheep[0]) <= pen_distX_var and abs(y-next_sheep[1]) <= pen_distY) :
                        pen_above.append((x,y))
                if next_sheep[1] < start_point[1]:
                    if ( abs(x-next_sheep[0]) <= pen_distX_var and abs(y-next_sheep[1]) <= pen_distY) :
                        pen_below.append((x,y))
                if next_sheep[0] < start_point[0]:
                    if ( abs(x-next_sheep[0]) <= pen_distX and abs(y-next_sheep[1]) <= pen_distY_var) :
                        pen_left.append((x,y))
                if next_sheep[0] > start_point[0]:
                    if ( abs(x-next_sheep[0]) <= pen_distX and abs(y-next_sheep[1]) <= pen_distY_var) :
                        pen_right.append((x,y))
        
        # choose the pen we captured the most sheep in, and move in that direction
        for pen in pen_above, pen_below, pen_left, pen_right :
            if len(pen) > len(cur_pen) :
                cur_pen = pen
                if pen == pen_above :
                    next_point = (start_point[0],start_point[1]+pen_distY)
                elif pen == pen_below :
                    next_point = (start_point[0],start_point[1]-pen_distY)
                elif pen == pen_left :
                    next_point = (start_point[0]+pen_distX,start_point[1])
                elif pen == pen_right :
                    next_point = (start_point[0]-pen_distX,start_point[1])
                else :
                    print "Houston we have a problem, we're not in a group"

        # recording the group       
        pens.append({"Pen%s" % (cur_pen_num) : cur_pen})

        # remove our penned sheep
        for sheep in cur_pen :
            my_sheep.remove(sheep)
        
        #reset our start point and loop
        start_point = next_point

    print " We found %s groups : " %( len(pens))
    print pens

if __name__ == "__main__":
    main()