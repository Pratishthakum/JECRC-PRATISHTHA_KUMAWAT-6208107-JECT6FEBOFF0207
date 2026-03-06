def update_max_speed(self, new_speed):
        self.max_speed = new_speed
        print(f'New Max Speed: {self.max_speed}')


TATA = Car(True, 'Level 5', '2L', 12, 100000)
print('Properties before updation:')
TATA.display_properties()
print()

print('Properties after updation:')
TATA.update_base_speed('60kmph')
TATA.update_max_speed('160kmph')
TATA.update_gears(5)
TATA.display_properties()



mahindra = Car(True, 'Level 4', '4L', 22, 250000)
print()
print('Mahindra: ')
mahindra.display_properties()



# self.prop_name

## constructor (__init__)

'''
class ClassName:
    properties
    
    def __init__(self, arg1, arg2, arg3, ..., argn):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        ...
        self.argn = argn
'''
