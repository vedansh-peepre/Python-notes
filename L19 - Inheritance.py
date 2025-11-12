# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 08:54:16 2025

@author: Hp
"""

#hello lec19 -- inheritance

# =============================================================================
# #Getters and setters (methods)
# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None
#     def __str__(self):
#         return "animal:" + str(self.name)+":" + str(self.age)
#     
#     #getters
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     
#     #setters
#     def set_age(self, new_age):
#         self.age = new_age
#     def set_name(self, new_name=""):
#         self.name = new_name
#         
#         
# #default parameters with methods        
# a = Animal(4)
# # print(a)
# b = Animal(6)
# # print(b)
# # print(a.age)
# # print(a.get_age())
# 
# # a.set_name("fluffy")
# # print(a.name)
# # print(a.get_name())
# # print(a)
# # a.set_name() #reverts to the origianl "None" that we created
# # print(a)
# 
# 
# #USING OUR CLASS
# 
# #YOU TRY IT
# 
# # Write a function that meets this spec.
# def make_animals(L1, L2):
#     """ L1 is a list if ints and L2 is a list of str
#         L1 and L2 have the same length
#     Creates a list of Animals the same length as L1 and L2.
#     An animal object at index i has the age and name
#     corresponding to the same index in L1 and L2, respectively. """
#     # your code here
#     #solution
#     L3 = []
#     for i in range(len(L1)):
#         #i is 0,1,2,3,4..
#         age = L1[i]
#         name = L2[i]
#         a = Animal(age)
#         a.set_name(name)
#         L3.append(a)
#     return L3
# 
# # L1 = [2,5,1]
# # L2 = ["blobfish", "crazyant", "parafox"]
# # animals = make_animals(L1, L2)
# # print(animals)     # note this prints a list of animal objects
# # for i in animals:  # this prints the indivdual animals
# #     print(i)
# =============================================================================


# Inheritence
class class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self);:
        return "cat:" + str(self.name) + ":" + str(self.age)
    
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_age(name)
        self.friends = []
    def get_friends(self):
        return self.friends.copy()
    def speak(self):
        print("hello")
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
