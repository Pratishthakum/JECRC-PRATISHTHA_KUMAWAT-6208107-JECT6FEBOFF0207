class Temp:
    def sum(self,a,b):
        print(a+b)

#to achieve method overloading we create another variable to hold that refrence 
    add_two_sum=sum 
    def sum(self,a,b,c):
        print(a+b+c)
obj=Temp()
obj.sum(12,20,30)
obj.add_two_sum(2,3)
#obj.sum(1,2,3)