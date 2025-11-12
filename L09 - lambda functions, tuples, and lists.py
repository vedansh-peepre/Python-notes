# def is_five(x):
#     return x==5
# print(is_five(6))
# print((lambda y: y==5)(5))

#YOU TRY IT
def do_twice(n, fn):
    return fn(fn(n))
print(do_twice(3, lambda x: x**2))