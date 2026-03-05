#set operations
s1={1,2,3}
s2={2,3,4}
s3=s1.union(s2)
print(s3)
s4=s1.union(s2,s3)
print(s4)
s5=s1.union({1,2,3},{4,5,6},{7,8,9})
print(s5)

s6=s1.intersection(s2)
print(s6)


ss7=s1.difference(s2)
print(ss7)


s7=s1.symmetric_difference(s2)  #basically it takes the unique elements from both the sets  rather than intersection and return them as a set of values
print(s7)
