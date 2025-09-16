# x=10
# p=0
# while ((2**p)*x )%1 != 0 :
#     print('Remainder = ' + str(   (2**p)*x - int(2**p)*x   ))
#     p+=1
    
# num=int((2**p)*x)

# result=""
# if num==0:
#     result="0"
# while num>0:
#     result= str(num%2) + result
#     num=num//2 

# for i in range(p - len(result)):
#     result='0'+result
# result= "0."+result
# print('Binary of ' + str(x) + " is " + str(result))  



#Approximation method
# x=36
# epsilon=0.01
# guess=0.0
# increment=0.0001
# num_guesses=0

# while abs(guess**2-x)>=epsilon:
#     guess+=increment
#     num_guesses+=1 

# print("num_guesses=", num_guesses)
# print(guess, "is close to square root of", x)
# or....

# =============================================================================
# x=54321
# epsilon=0.01
# guess=0.0
# increment=0.0001
# num_guesses=0
# 
# while abs(guess**2-x)>=epsilon and guess**2<=x:
#     guess+=increment
#     num_guesses+=1 
#     
# print('x='+ str(x))
# print("num_guesses=", num_guesses)
# if guess**2>=x:
#     print('failed to find the sqrt of',x)
#     print('last guess was',guess)
# else:
#     print(guess, "is close to square root of", x)
# =============================================================================

# =============================================================================
# #finger exercise for L5
# """Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your code should print out aceg."""
# 
# my_str = 'abcdefgh'
# # for i in range(len(my_str)):--> no it is noot the right way
# #i'm having issues recalling concatenation in strings
# # print(my_str[0:len(my_str+1):2])---> bhai ye bohot silly mistake hai 'len' ke andar hi +1 laga dena!
# print(my_str[0:len(my_str)+1:2])
# 
# # Here is the soöution:
# s = ''
# for i in range(0,len(my_str),2):
#  s += my_str[i]
# print(s)
# =============================================================================
