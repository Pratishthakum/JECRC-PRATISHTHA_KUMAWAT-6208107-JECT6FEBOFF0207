s='Python is a programming language'
print(s.lower())#returns value 

s1="python"

print(s.upper()) #convert it into uppercase letters

#print("pYTHON".capitalize())

print(s.lstrip())
print(s.rstrip())
print(s.strip())
print(s.title())
s2="Java"
print(s2.strip('J'))
print("Python".lstrip('o'))
print("Python".rstrip('P'))

print(s2.index('J'))
#print(s2.index('p'))
print(s2.replace('J','R'))
print(s2.find('p'))
print(s2.find('J'))
print(s2.find('c'))





s3="I LOVE -PYTHON -PROGRAMMING- LANGUAGE"
print(s3.split()) #gives list collection as a result 
print(s3.split('PYTHON')) 
print(s3.split('-'))
print('@'.join(s3))

s4="MY NAME IS PRATISHTHA"
print(s4.startswith('M'))
print(s4.endswith('A'))
print(s4.endswith('B'))


print(s4.isalpha())
print(s4.islower())
print(s4.isupper())
print(s4.isdigit())

s6="Pratishtha"
print(s6.isupper())
print(s6.isupper())








