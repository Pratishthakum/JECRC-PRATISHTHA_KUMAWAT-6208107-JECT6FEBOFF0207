#packing

# def func_name(*args):
#     Statement
#     Block 
#     func_name(val1,val2,.....,valn)

# create a function which can take n number of int or float numbers and return only their addition


def add_nums(*args):
    print(args,type(args))
    sum=0
    for i in args:
        sum+=i
    print(f'Addition: {sum}')
add_nums(1,2,3,4,5,1.9,98.2,1)

def add_nums(*args):
    args=list(args)
    print(args,type(args))
    sum=0
    for i in args:
        sum+=i
    print(f'Addition: {sum}')
add_nums(1,2,3,4,5,1.9,98.2,1)

#create a function which will take n no of inputs from the users and return the sum of only int and floating point numbers.Make sure thet user is capable of passing all type of values
def add_numbs(*args):
    print(args,type(args))
    sum=0
    
    for i in args:
        if type(i) in (int,float):
            sum+=i
    print(f'Addition:{sum}')
add_numbs(1,2,"hello",3.4,5.5,6)
        


def sum_numbers(*args):
    total = 0
    
    for value in args:
        if type(value) in (int, float):
            total += value
            
    return total
        




# def func_name(**kwargs):
#     Statement
#     Block 
# func_name(key1:val1,key2:val2....,keyn:valn)
# all the keyname should be string but u cant use 




def print_details(**kwargs):
    print(kwargs)
print_details(User_name="Pratishtha",age=23,password="12345",logged_in_devices=['Android','Windows','Linux'])





def add_int_float(*args):
    sum=0
    for i in args:
        if type(i) in (float,int):
            sum+=i
    print("sum is",sum)

add_int_float(*eval(input("enter a list of values : ")))
