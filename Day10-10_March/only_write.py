#file = open('temp1.txt' , 'w') create new text file if not present and then perform write operation
# file = open('temp.txt' , 'w') 
# # file.write('i am the new data') writing single line of data

# file.writelines([
#     'first line\n',
#     'second line\n',
#     'third line\n',
#     'third line\n',
#     'fourth line\n',
#     'fifth line\n',
#     'sixth line\n'
#     'hii there gud morning\n'

# ])

file = open('temp.txt' , 'w+') 


file.writelines([
    'first line\n',
    'second line\n',
    'third line\n',
    'third line\n',
    'fourth line\n',
    'fifth line\n',
    'sixth line\n'
    'hii there gud morning\n'

])
# file.seek(0)#to make the python interpreter to point at specific index,we use seek(index)
print(file.read())






# file.close()

#if the file is already present then it will override the previous data to new one
#









# file=open('notes.txt','r') # file not present we cant perform read operation
# print(file.read())

# file.close() 
