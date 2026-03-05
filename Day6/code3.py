s={1,2,3,4,5}
s.add(50)
print(s)



value=1
s.add(value)
print(s)#no changes would be there if i add the existing element

s={1,2,False,True,0,3+9j}

print(s)

s.add(100)
print(s)

value=2
s.add(value)
print(s)


print({1,2,False,True,0,3+9j}.add(2))

# s.add([1,2,3])  we cannot add mutable data inside the set collection
# print(s)


s.add('234')
print(s)
s.remove(3+9j)
print(s)
# print(s.remove(22))  this will throw error basically key error


s.discard('234')

print(s)

print(s.discard(22))#it will not throw any error if the element is not present


s.pop()
print(s)#randomly pop element 


s.clear()
print(s)
