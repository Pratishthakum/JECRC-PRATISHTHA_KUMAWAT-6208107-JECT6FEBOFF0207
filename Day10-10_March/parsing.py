## dumps(): encryption
## loads(): decryption

'''
1.JSON
2.pickle

'''



# import json
# file=open('temp.txt', 'a+')
# data={
#     'full_name':'pratishtha',
#     'user_id' : 87654,
#     'pasword' :'******'
# }
# # print(f'original data : {data}')
# # print(f'Type of original data : {type(data)}')
# # print()

# enc_data=json.dumps(data)
# file.write(enc_data)
# file.seek(0)
# enc_data=file.read()
# print(type(enc_data))

# ori_data=json.loads(enc_data)
# print(ori_data,type(ori_data))

# print(f'original data : {enc_data}')
# print(f'Type of original data : {type(enc_data)}')
# file.close()


import json

# file open
file = open('temp.txt', 'w+')

data = {
    'full_name': 'pratishtha',
    'user_id': 87654,
    'password': '******'
}

# python dict → json string
enc_data = json.dumps(data)

# write in file
file.write(enc_data)


file.seek(0)

# read from file
enc_data = file.read()
print(enc_data)
print(type(enc_data))

# json string → python dict
ori_data = json.loads(enc_data)
print(ori_data)
print(type(ori_data))

file.close()



import pickle

file = open('temp.text', 'wb+')

data = {
    'full_name': 'pratishtha',
    'user_id': 87654,
    'password': '******'
}


pickle.dump(data, file)

file.seek(0)


ori_data = pickle.load(file)

print(ori_data)
print(type(ori_data))

file.close()






