# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 23:38:33 2025

@author: Hp
"""

# Hello L14
# =============================================================================
# def find_grades(grades, students):
#      """ grades is a dict mapping student names (str) to grades (str)
#      students is a list of student names 
#      Returns a list containing the grades for students (in same order) """
#      # score=[]
#      # for i in grades:
#      #     if i == students:
#      #         score += grades['i']
#      # return score
#      
#      Lnew=[]
#      for elem in students:
#          #elem is Ana, then matt then john...
#          grade= grades[elem]
#          Lnew.append(grade)
#      return Lnew
     
# d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
# print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']
# =============================================================================
# =============================================================================
# def find_in_L(Ld, k):
#     """ L is a list of dictionaries
#     k is an int that we're searching
#     Returns True if k is a key in any dicts of L and false otherwise
#     """
#     for d in Ld:
#         #d is k1, v1, k2, v2, etc
#         if k in d:
#             return True  #breaks out of the func immediately
#     return False
#         
# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1, 3:9, 4:16, 5:25}
# 
# print(find_in_L([d1, d2, d3], 2))  # returns True
# print(find_in_L([d1, d2, d3], 25))  # returns False
# =============================================================================
# =============================================================================
# #YOU TRY IT
# def count_matches(d):
#     """ d is a dict
#     Returns how many entries in d have the key equal to its value """
#     # your code here
#     count = 0
#     for k,v in d.items():
#         #star cide, k binds to key and v binds to value
#         if k == v:
#             count += 1
#     return count
#     # #other way
#     # count=0
#     # for x in d:
#     #     if d[x]==x:
#     #         count+=1
#     # return count
# #correct!
# 
# d = {1:2, 3:4, 5:6}
# print(count_matches(d))   # prints 0
# 
# d = {1:2, 'a':'a', 5:5}
# print(count_matches(d))   # prints 2
# =============================================================================
