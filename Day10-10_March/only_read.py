file=open('temp.txt', 'r')
'''
1.read(): display the file content as it is
2.readline(): display single line of data at a time
3.readlines()

'''
print(file.read())
file.seek(0)

print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readlines())

file.seek(0)


file.close()
