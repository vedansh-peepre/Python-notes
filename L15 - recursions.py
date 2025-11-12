# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 14:40:59 2025

@author: Hp
"""

#Hello L15-Recursions

#recurcide multiplication-
def mult_recur(a, b):
    if b==1:
        return a 
    else:
        return a + mult_recur(a, b-1)
# print(mult_recur(5, 4))

# =============================================================================
# ############### YOU TRY IT #################
# # Calculate n**p recursively by writing this function
# def power_recur(n, p):
#     if p==0 :
#         return 1
#     elif p==1 :
#         return n
#     else:
#         return n * power_recur(n, p-1)
# 
# print(power_recur(2,3))  # prints 8
# =============================================================================
def fact(n):
    if n<=1:
        return 1
    else:
        return n * fact(n-1)
print(fact(4))

#and iteratively, factorial can be calculated...
def fact_iter(m):
    prod=1
    for x in range(1, m+1):
        prod *= x
    return prod
print("by iteration, it is also", fact_iter(4))