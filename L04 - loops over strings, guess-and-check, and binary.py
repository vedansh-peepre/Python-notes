# mysum=0
# for i in range(5,11,2):
#     mysum+=i 
#     if mysum==5:
#         break
#         mysum+=1
#         #this never gets executed!
# # print(mysum)

# even_nums=0
# for i in range(5):
#     # i is 0,1,2,3,4
#     if i%2==0:
#         even_nums+=1
# print(even_nums)

#here are 3 ways to iterate the same thing...
# s="demo loops  - fruit loops"
# for index in range(len(s)):
#     if s[index]=="i" or s[index]=="u":
#         print("There is an i or u")
# print('--------')
# for char in s:
#     if char=='i' or char=='u':
#         print("There is an i or u")
# print('--------')
# for char in s:
#     if char in 'iu':
#         print("There is an i or u")

# an_letters="aeiou"
# word=

#You have been givn a string that counts how many unique letter are there in a word. For instance, in string "abca" number==3
#idea in notebook (s~)
# s="abca"
# seen=""
# count=0
# for char in s:
#     if char not in seen:
#         seen=seen+char
#         count+=1
# print(count)

# finding sqrt by guess-and-check algoritm
# x=int(input('Enter a positive integer'))
# guess=0
# neg_flag=False
# while guess**2<x:
#     guess+=1
# if x<0:
#     neg_flag=True
# if guess**2==x:
#     print(f'The sqrt of {x} is {guess}')
# else:
#     print(x,'is not a perfect square')
#     if neg_flag==True:
#         print(f'just checking... did you mean {-x}')

#you try it section
# secret=int(input("give me the number, I'll try and guess it"))
# secret=4
# found=False
# # guess=""
# for i in range(11):
#     if i==secret:
#         found=True
# #         guess==i
# #         print(f'Your secret number is {guess}')
# #     else:
# #         pass
# # if guess=="":
# #     print("I didn't find the number")
# if found:
#     print('found')
# else:
#     print('not found')

# =============================================================================
# #binary
# num=1507
# result=""
# if num==0:
#     result="0"
# while num>0:
#     result = str(num%2) + result
#     num=num//2
# print(result)
# =============================================================================
# =============================================================================
# #finger exercise of L4
# 
# """Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube root of N. The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. Hint: use a loop that increments a counter—you decide when the counter should stop."""
# 
# N = 9
# for i in range(N+1):
#     if i**3 == N:
#         print(f'{N} is a perfect cube. {i} cube is {N}.')
# else:
#     print(f'{N} is not a perfect cube.')
# =============================================================================
