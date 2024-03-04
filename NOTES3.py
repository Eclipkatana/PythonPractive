class Car:
    def __init__(self, make, model):
        #! Instance attribute
        self.make = make
        self.model = model
    
    #! when read code, if see something like this with "_" , dont change it. its a private attribute    
    #self._id = 5

#! hasattr() and setattr() and getattr()
car = Car("Toyota", "Corolla")
print(hasattr(car, "make")) #! check if the object has the attribute

setattr(car, "weapon", "gun") #! set the attribute
print(car.weapon)


#! Pass tells python to ignore the line, not do anything with it
#! Add this to a function which dont have any code yet
def test():
    pass

#! decorators
def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

#! this is the function that will be decorated
@my_decorator #! this is needed to call the decorator, dont need this for traditional way
def create_asterisk_house():
    print('')
    print('   /\\   ')
    print('  /  \\  ')
    print(' /    \\ ')
    print('/______\\')
    print('|      |')
    print('|      |')
    print('|______|')
    print('')
    
#! traditional way to use decorator
#my_decorator(create_asterisk_house)()

#! this is another way to use decorator, must have the @my_decorator above the function
create_asterisk_house()