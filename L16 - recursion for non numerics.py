# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 07:46:34 2025

@author: Hp
"""

#Hello L16 recusions for non-numerics
def fib(x):
    if x == 1 or x == 2:
        # count1+=1
        return 1
    else:
        # count1+=1
        return fib(x-1) + fib(x-2)
    # print(f'count1={count1}')

def fib_efficint(n, d):
    if n in d:
        # count2+=1
        return d[n]
    else:
        # count2+=1
        ans = fib_efficint(n-1, d) + fib_efficint(n-2, d)
        d[n] = ans
        return ans
    # print(f'count2={count2}')
    
fib_dict = {1:1,2:1}
# print(f"fib(6) = {fib(6)}")
# print(f"by fib efficient = {fib_efficint(6, fib_dict)}")

# print(fib(34)) #makes 11 million calls!!
# print(fib_efficint(34, fib_dict)) #makes just 65 calls


def score_count(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 3
    else:
        return score_count(x-1) + score_count(x-2) + score_count(x-3)
    
# print(score_count(5))  #-- Beware! it may take too much power and time, so Ctrl+C

def total_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + total_recur(L[1:])
# print(total_recur([10,20,30,40,50,60]))

def total_len_recur(L):
    if len(L) == 1:
        #eg ["ab"]
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])
    
test = ["ab", "c", "defgh"]
# print(total_len_recur(test))  # prints 8

#BC jab ses iske chakkar me atka tha, abhi dekha total_recur ko call kar raha tha q_q

# L1= ['a', 'b', 'c']
# s1 = "".join(L1)   # A way but we have to use recursion here
# print(s1)

def flatten_iter(L):
    newL = L[:]
    L.clear()
    for i in range(len(newL)):
        # print(L)
        L += newL[i]
    return L

List1 = [[1,2],[3,4],[9,8,7]]
# print(flatten_iter(List1))

def in_lists_of_list(L, e):
    """
    L is a list whose elements are lists containing ints
    Returns True if e is an element within the lists of L
    and False otherwise. 
    Hint, the in operator is useful here, i.e. e in something
    """
    # your code here
    # if len(L) == 1:
    #     if type(L[0]) == int():
    #         return L[0] == e
    #     else:
    #         return in_lists_of_list(L[0], e)
    # else:
    #     if type(L) == int():
    #         return in_lists_of_list(L[1:], e)
    #     else:
    #         return            
    #     # return in_lists_of_list(L[1:], e)
    
    #solution-
    if len(L) == 1:
        return e in L[0]
    else:
        first = L[0]
        if e in first:
            return True
        else:
            return in_lists_of_list(L[1:], e)
        
        
test = [[1,2], [3,4], [5,6,7]]
# print(in_lists_of_list(test, 3))  # prints True

test = [[1,2], [3,4], [5,6,7]]
# print(in_lists_of_list(test, 0))  # prints False

def my_rev(L):
    if len(L) == 1:
        return L
    else:
        return my_rev(L[1:]) + [L[0]]  #note this is a list and we're concatenating here
    
def my_advanced_rev(L):
    """ here we'll reverse the elements, but if the elements is 
    a list itself, the we will reverse that sublist as well. """
    if len(L) == 1:
        if type(L[0]) != list:
            return L
        else:
            return [my_advanced_rev(L[0])]  #again sq brackets cuz we wanna retrn list to concatenate
    
    else:
        if type(L[0]) != list:
            return my_advanced_rev(L[1:]) + [L[0]]
        else:
            return my_advanced_rev(L[1:]) + [my_advanced_rev(L[0])]
        
ptest = [[1,2], [[8,5], [7,6]], [3,4], [5,6,7]]
print(my_advanced_rev(ptest))        
        
        
        
        
        
        
####### QUESTIONS #######
# Q1. Memoize the code to find possible scores in basketball
def score_count_2(x, d):
    pass
    
d = {1:1, 2:2, 3:3}
# print(score_count(4, d))  # prints 6
# print(score_count(6, d))  # prints 20
# print(score_count(13, d))  # prints 1431

# Q2. 
def in_list_of_lists_mod(L, e):
    """
    L is a list whose elements are either
        * lists containing ints or
        * ints
    Returns True if e is an element within L or 
    sublists of L and False otherwise. 
    """
    # your code here


# test = [[1,2],3,4,5,6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 3))  # prints True
# test = [[1,2],[3,4,5],6,7]
# print(in_list_of_lists_mod(test, 10))  # prints False

# Q3. 
def my_deepcopy(L):
    """ 
    L is a list, containing lists or list of lists, etc.
    Returns a new list with the same structure as L that 
    contains copies (recursively) of every sublist 
    """
    # your code here

# myL = ["abc", ['d'], ['e', ['f', 'g']]]
# my_newL = my_deepcopy(myL)
# print(myL)
# print(my_newL)
# myL[2][1][0] = 1
# print(myL)      # should be ['abc', ['d'], ['e', [1, 'g']]]
# print(my_newL)  # should be ['abc', ['d'], ['e', ['f', 'g']]]


# Q4. Here are 3 recursive functions that are incorrectly implemented.
# Debug them to have them do what the specs say.
def f(L):
    """ L is a non-empty list of lowercase letters.
    Returns the letter earliest in the alphabet. """
    if len(L) == 1:
        return L[0]
    else:
        if L[0] < f((L[0])):
            return L[0]
        
# print(f(['z', 'a', 'b', 'c', 'd']))  # should print 'a'


def g(L, e):
    """ L is list of ints, e is an int
    Returns a count of how many times e occurrs in L  """
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        if e == L[0]:
            return 1
        else:
            return 0
    else:
        if L[0] == e:
            1+g(L[1:], e)
        else:
            return 1
    
# print(g([1,2,3,1], 1))     # should print 2
# print(g([1,1,2,3,1,1], 1)) # should print 4
    

def h(L, e):
    """ L is list, e is an int
    Returns a count of how many times e occurrs in L or 
    (recursively) any sublist of L
    """
    if len(L) == 0:
        return 0
    else:
        if type(L[0])==int:
            if L[0] == e:
                return 1+h(L[1:], e)
            else:
                return h(L[1:], e)
        elif type(L[0])== list:
            return h(L[1:], e)
    
# print(h([1,2,[3],1], 1))        # should print 2
# print(h([1,2,[3,1,[1,[1]]]], 1))  # should print 4
    
#####################################################    