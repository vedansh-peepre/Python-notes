# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 18:57:55 2025

@author: Hp
"""

# =============================================================================
# #list comprehensions
# # [expression for elem in iterable if test] is equivalent to-
# def f(expr, old_list, test = lambda x: True):
#     """expr is a function
#     old_list is an iterable
#     test is a test for fn lambda"""
#     new_list=[]
#     for e in old_list:
#         if test(e):
#             new_list.append(expr(e))
#     return new_list
# 
# print(f(e**2, [0,1,2,3,4,5,6,7,8], e%2==0))
# print([e**2 for e in range(6)])
# print([ [e, e**2] for e in range(4) if e%2 != 0 ])
# 
# =============================================================================
test = [11,22,33]
print(test[4]) #IndexError