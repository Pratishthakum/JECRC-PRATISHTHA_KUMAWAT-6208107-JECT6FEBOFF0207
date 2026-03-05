#create a function which will return  a list of prime numbers.Please make sure that user can pass n number of inputs.For checking whether  a number is prime or not , you can create a function



# def isPrime(num):
#     return True or False

# def find_prime_num(*args):
#     prime=[]
#     for num in args:



#     return prime
# find_prime_num(*eval(input("enter a list of nums: ")))









def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True


def find_prime_num(*args):
    prime = []
    
    for num in args:
        if type(num) == int and isPrime(num):
            prime.append(num)

    return prime


print(find_prime_num(*eval(input("enter a list of nums: "))))




