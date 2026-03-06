class Car:

    wheelers=4
    engine="Petrol"
    base_speed="40Km/hr"
    max_speed="120km/hr"
    gears=4

TATA=Car()
TATA.engine=["Petrol","Diesel","EV"]
TATA.airbags=True
TATA.no_of_airbags=4
TATA.base_budget='2L'
TATA.no_of_varient=12


def __init__(self, air_bags,security,base_budget,varient,total_sale):
    self.air_bags=air_bags
    self.security=security
    self.base_budget=base_budget
    self.varient=varient
    self.total_sale=total_sale


    @classmethod
    def update_gears(cls,new_gears):
        cls.gears=new_gears
        print(f"no of gears: {cls.gears}")

def display_properties(self):
    print(
        {
            'air_bags': self.air_bags,
            'security':self.security,
            'base_budget':self.base_budget,
            'varient':self.varient,
            'total_sale':self.total_sale
        }
    )

def  update_base_speed(self, new_base_speed):
    self.base_speed=new_base_speed
    print(f"New base speed : {self.base_speed}")

def update_max_speed(self,new_speed):
    self.max_speed=new_speed
    print(f"New max speed:{self.max_speed} ")

TATA=Car(True,'level 5','2l',12,10000000)

TATA.display_properties()
Mahindra=Car(True,'level 4','4l', 20, 2500000)
Mahindra.display_properties()
print()


print("properties after updation")
TATA.update_base_speed("6okm/hr")
TATA.update_max_speed("130km/hr")
TATA.update_gears(5)
TATA.display_properties()






#constructor---magic method (__init__)
#used to initialize a state of object

# class ClassName:
#     properties

#     def __init__(self,arg1,arg2,arg3,.......,argn)
#         self.arg1=arg1
#         self.arg2=arg2
#         self.argn=argn

