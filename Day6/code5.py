#dictionary operations

dict1={1:1,2:2,(1,2,3):(1,2,30)} #immutable lega
print(dict1.get(2))


print(dict1.get((1,2,3)))

print(dict1[(1,2,3)])

dict1.pop(1)
print(dict1)

dict1.pop(2,(1,2,3))
print(dict1)


#pop items ----> pop last key:value pairs in LIFO order
user={"username": "pratishtha",
    "password":"*****", 
    "location":"India"}
user.popitem()#give key error if all the items are poped out
print(user)
user.popitem()
print(user)
user.popitem()
print(user)
# user.popitem()
# print(user)   give key error now

user['password']='123'
print(user)

user.update({'password':'1234','is_loggedIn':True})#override the existing one and adding new key:value pair
print(user)

print(user.keys())
print(user.items())
