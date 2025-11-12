# def add(a,b):
#     return a+b
# def mult(a,b):
#     print(a*b)

# add(1,2)
# print(add(2,3))
# mult(3,4)
# print(mult(4,5))


#YOU TRY IT
# def is_triangular(n):
#     """n is an int>0
#     returns True if n is triangular, i.e. equals to summation of natural nos (1+2+3+...+k). and False otherwise
#     """
#     total = 0
#     for i in range(n+1):
#         total += i
#         if total == n:
#             return True 
#             # break
#     return False
#     # print(total)
        
# print(is_triangular(6))

#FOR BISECTION ROOT
# def bisection_root(x):
#     epsilon=0.00000000000001
#     low=0
#     high=x 
#     ans = (high+low)/2.0 
#     while abs(ans**2-x) >= epsilon:
#         if ans**2 < x:
#             low = ans
#         else:
#             high = ans
#         ans = (low+high)/2.0 
#     return ans

# print(bisection_root(1048576))

#YOU TRY IT 
def calc (op, a, b):
    return op(a,b)

def div (a,b):
    if b!=0:
        return a/b 
    print('denom was 0')
    # return None
    
res = calc (div, 2, 0)