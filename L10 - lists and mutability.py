# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 19:47:58 2025

@author: Hp
"""

# =============================================================================
# L= [2,1,3]
# L.append(5)
# # L=L.append(5)
# print(L)
# 
# #YOU TRY IT
# L1= ['re']
# L2= ['mi']
# L3= ['do']
# L4= L1 + L2
# L3.append(L4)
# L= L1.append(L3)
# print(L)
# print(L1)
# 
# =============================================================================
# =============================================================================
# # def make_ordered_list(n):
# #     """n is a positive int
# #     Returns a list containing all ints in order 
# #     from 0 to n [inclusive]
# #     """
# #     mylist=[]
# #     for i in range(n+1) :
# #         mylist.append(i)
# #     return mylist
# 
# # print(make_ordered_list(6)) #prints [0,1,2,3,4,5,6]
# 
# =============================================================================

# =============================================================================
# another
# def remove_elem(L, e):
#     """
#     L is a list
#     Returns a new list with elements in the same order as L but completely deleting elements equal to e
#     """
#     # index=0     #my try
#     # values=[]
#     # for i in L:
#     #     index+=1
#     #     if i == e:
#     #         values+=index
#     #     else:
#     #         pass
#     
#     newlist=[]
#     for i in L:
#         #i is 1 tehn 2 then 2 then 2
#         if i != e:
#             newlist.append(i)
#     return newlist
#     
# L = [1,2,2,2]
# print(remove_elem(L, 2))
# print(remove_elem(L, 1))
# print(remove_elem(L, 0))
# =============================================================================

# =============================================================================
# # def count_words(sen):
# #     """ sen is a string and this fn returns number of words"""
# #     L1 = sen.split(' ')
# #     return len(L1)
# 
# # print(count_words('hey jude'))
# 
# =============================================================================
# =============================================================================
# # def sort_words(sen):
# #     """sen is string repreasenting a semtence 
# #     REturns a list containing all the words in sesn but sorted in alplabetical order."""
# #     L = sen.split(' ')
# #     L.sort()
# #     return L
#     
# # s = 'look at this photograph'
# # print(sort_words(s))  #prints ['at', 'look', 'phtoograph', 'this']
# 
# =============================================================================
# =============================================================================
# # def square_list(L):
# #     for i in range(len(L)):
# #         L[i] = L[i]**2
# 
# # lin=[2,4,8]
# # print('lin before mutation', lin)
# # square_list(lin)
# # print('lin after mutation', lin)
# =============================================================================
# =============================================================================
# L=[1,2,3,4]
# i=0
# for e in L:
#     L.append(e)
#     i+=1
#     dontprint(L)     #its infinite execution
# =============================================================================
