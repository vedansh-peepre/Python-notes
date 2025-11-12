# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 00:13:45 2025

@author: Hp
"""

# lecture 8
# =============================================================================
# #YOU TRY IT
# def remove_all(L, e):
#     """
#     L is a list
#     mutates L to remove all elements in L that're equal to e
#     Returns none --> this is different from what we had in l10
#     """
#     # mylist=[]
#     # for i in L:
#     #     if i != e:
#     #         mylist += i      -->previous mehod[lecture 10]
#     
#     L_copy = L[:]
#     L.clear()
#     for n in L_copy:
#         if e != n:
#             L.append(n) 
#            
#     
# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)
# 
# Lin = [1,2,2,2]
# remove_all(Lin, 1)
# print(Lin)
# =============================================================================
# L = [0,2,5,6,1,8]
# # a = L.pop()
# print(L, L.pop())

def remove_dups(L1, L2):
    L1_copy=L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
    return L1

la= [10,20,30,40]
lb=[10,20,50,60]
print(remove_dups(la, lb))