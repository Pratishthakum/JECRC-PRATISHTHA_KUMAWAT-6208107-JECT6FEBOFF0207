import time
#approaches of handling exception


# 1. Specific Exception handling:we know about exception and error that might occur during execution of code

#print(10/0) give zero division error
'''
try:
    problem
    Statement
except ErrorName:
    resolution/
    solution code
'''


# n1,n2=21,0


# try:
#     result=n1/n2
#     print(result)
# except ZeroDivisionError:
#     #solution code
#     print('please do not choose 0 as second num')


# print('code after try except-01')
# print('code after try except-02')
# print('code after try except-03')

# try:
#     a,b,c=1,2
# except ValueError:
#     print("for performing MVC no of variables should be equal to no of values!!!!")

# try:
#     print(a,b,c)
# except NameError:
#     print("identifiers are not there in the memory")

'''

2. Generic Exception Handling:it is a type of exception handling approach in which there is no need to pass any particular exception class name instead of we can use parent exception class called "Exception" and it automatically handles the situation

#drawback is using generic EH we cant handle keyboard interruption

'''
# try:
#     a,b,c=1,2
# except Exception:
#     print("for performing MVC no of variables should be equal to no of values!!!!")

# try:
#     print(a,b,c)
# except Exception:
#     print("identifiers are not there in the memory")



# try:
#     while True:
#         print(time.time())
# except Exception:
#     print("loop got stopped")


#default exception handling: we can handle all type of error with keyboard interruption exceptions except "Syntax error"
# try:()
#     while True:
#         print(time.time())
# except:
#     print("loop got stopped")







#raise---> it is a keyword which help us to throw an error in between the paragraph

'''

Exception creation

1.custom exception(raise)
2.user-defined exception(raise)
3.assertion exception(assert)


custom exception:
we use prebuilt exception classes acc to our requirement

we use raise k/w

raise ValueError('message')

ValueError: message


'''


# num=11
# if num>=18:
#     print('eligible for voting and driving')
# else:
#     raise NameError('age should be greater than or equal to 18')
#     #raise ValueError('age should be greater than or equal to 18')




'''

user defined exception:

1.it is atype of exception in which we can create our own exception classess based upon our own requirement we can also provide names of those classes acc to user cases


'''



# class MyException(Exception):
# #     pass

# #raise MyException('this is my exception class')

# n1,n2=10,0
# if n2==0:
#     raise MyException('second num cannot be 0')
# else:
#     print(n1/n2)



'''

assertion exception:
assertion exception can be created by using one keyword calles "assert"

assert<condition>,print(ERROR)
print(output)
'''


s=input('enter a string: ')
assert s==s[::-1], print('it is not a palindromic string')
print('it is a palindromic string')













