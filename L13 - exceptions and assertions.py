# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 13:58:44 2025

@author: Hp
"""
# =============================================================================
# 
# #YOU TRY IT
# def pairwise_div(Lnum, Ldeno):
#     """ Lnum and Ldeno are non empty lists of equal lengths containing numbers
#     
#     returns a new list whose elements are the pairwise division of an element in Lnum by an elem in Ldeno
#     
#     raise a ValueError if Ldeno contains 0."""
#     
#     assert len(Lnum)==len(Ldeno), "lengths are different"
#     assert len(Lnum)!=0, "the lists are empty"
#     
#     part = []
#     for i in range(len(Lnum)):
#         try:
#             part.append(Lnum[i] / Ldeno[i])
#         except ZeroDivisionError:
#             raise ValueError('input contains a zero')
#     return part
#     
# # # For example:
# # L1 = [4,5,6]
# # L2 = [1,2,3]    
# # print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]
# 
# # L1 = [4,5,6]
# # L2 = [1,0,3]    
# # print(pairwise_div(L1, L2))  # raises a ValueError
# 
# ## to run after introducing assertions
# # L1 = [4,5,6,7,8]
# # L2 = [1,8,3]    
# # print(pairwise_div(L1, L2))  # raises an AssertionError
# 
# # L1 = []
# # L2 = []    
# # print(pairwise_div(L1, L2))  # raises an AssertionError→
# =============================================================================

# finger exercisse
def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # # Your code here  
    # sum = 0
    # for elem in L:
    #     if elem is str or list:
    #         sum+=int(elem)
    #     # if elem is list:
    #         # for i in elem:
    #             # if i is str:
    #                 # sum+=i
    #     else:
    #         raise ValueError('The list contains elem other than string or list')
    # return sum



    # Solution
    total = 0
    for i in L:
        if type(i) == str:
            total += len(i)
        elif type(i) == list:
            for e in i:
                if type(e) == str:
                    total += len(e)
                else:
                    raise ValueError
        else:
            raise ValueError
    return total   #Damn its good-ly written

# Examples:
# print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
# print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
# print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError