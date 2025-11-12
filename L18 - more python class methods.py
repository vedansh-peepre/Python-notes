# hello L18 - more python class methods

class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq - y_diff_sq)**.5
    
# class Circle(object):
#     def __init__(self, center, radius):
#         self.center = center
#         self.radius = radius

# point = Coordinate(2, 2)
# my_circle = Circle(point, radius=5)


# =============================================================================
# #YOU TRY IT!
# 
# """Add code to the init method to check that the type of center is
# a Coordinate obj and the type of radius is an int. If either are
# not these types, raise a ValueError."""
# 
# class Circle(object):
#     def __init__(self, center, radius):
#         self.center = center
#         self.radius = radius
#         if type(center) == Coordinate and type(radius) == int:
#             pass
#         else:
#             raise ValueError("Center should be a coordinate obj. Radius should be an int")
#     def is_inside(self, point):
#         """returns True if point is inside the cirle, False otherwise"""
#         return point.distance(self.center) < self.radius
# 
# O = Coordinate(2, 2)
# my_circle = Circle(O, radius=2)
# 
# # p = Coordinate(1, 1)
# p = Coordinate(10, 10)
# print(my_circle.is_inside(p))
# # print(my_circle.is_inside(r))
# 
# # print(my_circle.center)
# # print(my_circle.radius)
# =============================================================================

# =============================================================================
# #EXAMPLE: FRACTION
# class SimpleFraction(object):
#     """ A number represented as a fraction """
#     def __init__(self, num, denom):
#         """ num and denom are integers """
#         self.num = num
#         self.denom = denom
#     
#     def times(self, oth):
#         top = self.num * oth.num
#         bottom = self.denom * oth.denom
#         return top/bottom
#     
#     def plus(self, oth):
#         top = self.num*oth.denom + self.denom*oth.num
#         bottom = self.denom * oth.denom
#         return top/bottom
#     
# ########## YOU TRY IT! ##########
#     def get_inverse(self):
#         """ Returns a float representing 1/self """
#         # your code here
#         return self.denom / self.num
#         
#     def invert(self):
#         """ Sets self's numerator to its denominator and vice versa.
#             Returns None. """
#         # your code here
#         # temp = 0
#         temp = self.num
#         self.num = self.denom
#         self.denom = temp
#         # other way
#         # (self.num, self.denom) = (self.denom, self.num)
#         
# ########## dunder methods ##########
#     def __str__(self):
#         # return str(self.num) + "/" + str(self.denom)
# # but, to make it so that 4/1 prints 1,
#         if self.denom == 1:
#             return str(self.num)
#         else:
#             return str(self.num) + "/" + str(self.denom)
#         
#         
# # f1 = SimpleFraction(3,4)
# # print(f1.num, f1.denom)   # prints 3 4 
# # print(f1.get_inverse())   # prints 1.33333333 (note this one returns value)
# # f1.invert()               # acts on data attributes internally, no return
# # print(f1.num, f1.denom)   # prints 4 3
# 
# 
# f1 = SimpleFraction(4, 3)
# f2 = SimpleFraction(5, 1)
# print(f1)
# print(f2)
# =============================================================================

# IMPLIMENTING MORE DUNDER METHODS
class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def __str__(self):
        return str(self.num) + "/" + str(self.denom)
    def __mul__(self, oth):
        top = self.num * oth.num
        bottom = self.denom * oth.denom
        return Fraction(top, bottom)
    
    
a = Fraction(1,4)
b = Fraction(3,4)
product = a*b 

print(a)
print(b)
print(product)


class Fraction(object):
    def reduce(self):
        def gcd(n, d):
            while d != 0:
                (d, n) = (n%d, d)
            return n
        if self.denom == 0:
            return None
        elif self.denom == 1:
            return self.num
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num/greatest_common_divisor)
            bottom = int(self.denom/greatest_common_divisor)
            return Fraction(top, bottom)