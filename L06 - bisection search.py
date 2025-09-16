#BISECTION SEARCH
# x=.5
# epsilon=0.01
# num_guesses=0
# if x<1:
#     low=0
#     high=1.0 
# else:
#     low=0.0
#     high=x 
# guess=(high+low)/2.0 
# while abs(guess**2-x) >= epsilon:
#     if guess**2<x:
#         low=guess
#     else:
#         high=guess
#     guess=(high+low)/2.0 
#     num_guesses+=1
# print("num_guesses="+str(num_guesses))
# print(guess, "is the sqrt of", x)

#For cubes
# x=27
# epsilon=0.01
# low=0
# high=x
# num_guesses=0
# guess=(high+low)/2.0 

# while abs(guess**3-x)>epsilon:
#     if guess**3 > x:
#         #too high
#         high=guess
#     else:
#         low=guess
#     guess= (high+low)/2.0 
#     num_guesses+=1 
# print("num_guesses=", num_guesses)
# print("the cube root of", x, "is", guess)

# =============================================================================
# #Newton rhapson
# epsilon=0.01
# k= 24.0
# guess= k/2.0 #can take any!
# num_guesses=0 
# 
# while abs(guess**2 - k) >= epsilon:
#     num_guesses += 1 
#     guess = guess - ((guess**2-k)/(2**guess))
# print("num_guesses=", num_guesses)
# print("the sqrt of", k, "is about", guess)
# =============================================================================

# =============================================================================
# #Finger exercise for L6
# """Assume you are given an integer 0 <= N <= 1000.
# Write a piece of Python code that uses bisection search to guess N. The code prints two lines 'count' with how many guesses it took to find N, and 'answer' with the value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one."""
# 
# N=25
# 
# low=0
# high=1000
# epsilon=0.01
# guess=(low + high)/2.0
# count = 0
# 
# while abs(N-guess) >= epsilon:
#     if guess > N:
#         #too high
#         high = (low+high)/2.0
#     elif guess < N:
#         #too low
#         low = (low+high)/2.0
#     guess=(low + high)/2.0
#     count+=1
# print(count)
# # print(guess)
# print('is you number', guess, '?')
# =============================================================================
