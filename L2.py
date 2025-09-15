f='a'
g=" b"
h="3"
s2=(f+g+" ")*int(h)
print(s2)

a= float(input("type first number"))
b= float(input("type second number"))
summ= a+b
product= (a*b)  
part= a/b
# print("sum=",summ)
print("sum="+str(summ))
print("product=",product)
print("part=",part)

# syntax errror is happening because the input is a string. but this can be tackled by just casting the input to float or int. Otherwise will have to do casting in individual object while doing arithmetic...
# another issue may arise! when printing, for concatenating string and float or int, we can only use 'comma' or we'll have to first convert the sum/product/part to string first. eg. summ_str= string(summ)

question=input("choose a verb:")
print('I can',question, 'better than you!')
print((question+" ")*5)

test1= 2>3
test2= 3<4
print(test1)
print(test2)
print(test1 and test2)
print(test1 or test2)

secret= 5
guess= int(input('Please guess a number'))
# print(secret==guess)
if guess == secret:
    print("Great! Your guess is equal to my secret number")
elif guess > secret:
    print("Your guess is greater than my number")
else:
    print("Your guess is smaller than my number")

# Debug early, debug often. Write a little and test a little. Don’t write a complete program at once. It introduces too many errors. Use the Python Tutor to step through code when you see something unexpected!
print("This is the end of lecture 2. さよなら、じゃあね")