def is_even (i):
    """
    Input is a positive int 
    it'll return True if i is even, otherwise False
    """
    if i%2 == 0:
        return True
    else:
        return False
    return i%2 == 0 #simplified! NOTE: we only defined it now
    
# print(is_even(3))
# print(is_even(8))


#YOU TRY IT EXERCISES
# def div_by (n, d):
#     """n and d are ints>0
#     Returns True if d divides n completely and False otherwise"""
#     return n%d == 0
    # return d%n == 0   #--> this is wrong in our context
# print(div_by(10, 3))
# print(div_by(10, 2))
# print(div_by(195, 13))

print("Numbers b/w 1 and 10: even or odd?")
even_nos=""
odd_nos=""
for i in range(1, 11):
    if is_even(i):
        print(i, "even")
        even_nos = even_nos + str(i) + " "
    else:
        print(i, "odd")
        odd_nos = odd_nos + str(i) + " "
print(f'even_nos= {even_nos}')
print(f'odd_nos= {odd_nos}')
