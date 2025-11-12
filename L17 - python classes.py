# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 08:11:34 2025

@author: Hp
"""

#Hello L17- Python classes

# =============================================================================
# class Coordinate(object):
#     def __init__(self, xval, yval):
#         """self is a parameter that lets us create variables 
#         unique to the object"""
#         self.x = xval
#         self.y = yval
#         
# c = Coordinate(3,4)    #associates self to c
# origin = Coordinate(0,0)
# 
# # print(c.x) #grabs variable associated with self.x and 'cuz self was associated to c before here
# # print(origin.y)
# =============================================================================

class Coordinate(object):
    def __init__(self, xval, yval):
        """self is a parameter that lets us create variables 
        unique to the object"""
        self.x = xval
        self.y = yval
    def distance(self, other):     # distance between two points in cartesian plane using distance formula aka pythagoras theorem
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq - y_diff_sq)**0.5
    
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
    
conventional = c.distance(origin)
equivalent = Coordinate.distance(c, origin)

print(conventional)
print(equivalent)