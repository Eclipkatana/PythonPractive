
#! Class and Object
class monster:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    def attack(self, target):
        target.hp -= self.atk
        print(self.name, "attacks", target.name, "for", self.atk, "damage!")
    def is_alive(self):
        return self.hp > 0
    
    
    
dragon=monster("Dragon", 100, 20)
snake=monster("Snake", 5, 10)
print(dragon.attack(snake))

#! Dunder method
class Book:
    #! Called when object is created
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    #! Called when str() is called
    def __str__(self):
        return f"{self.title} by {self.author}"
    #! Called when len() is called
    def __len__(self):
        return self.pages
    #! Called when del() is called
    def __del__(self):
        print("A book object has been deleted")
        
#%% #! test1
health = 50
def update_health(health,amount):
    health += amount
    return health

print(update_health(health,20))
# %%

#%% #! Simple Inheritance example, 1 child class inherit from 1 parent class
class monster:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        print(self.name, "has", self.hp, "hp and", self.atk, "atk!")
        
    def attack(self, target):
        target.hp -= self.atk
        print(self.name, "attacks", target.name, "for", self.atk, "damage!")
        print(target.name, "has", target.hp, "hp left!")
    
    def is_alive(self):
        return self.hp > 0
    
    #! Inheritance Monster class, put the parent class in the parameter
class shark(monster):
    def __init__(self, name, hp, atk, speed):
        #! get parent class attributes using super()
        super().__init__(name, hp, atk)
        self.speed = speed
    
    def set_speed(self, speed):
        self.speed = speed
        
    def swim(self):
        print("The shark swims at", self.speed, "mph!")

dragon=monster("Dragon", 100, 20)        
shark1 = shark("Shark", 50, 10, 20)

print(shark1.swim())

print(shark1.attack(dragon))
# %% #! Complex Inheritance example, 1 child class inherit from 2 parent class, follow the mro order, to find where to put super().__init__(). 
class monster:
    def __init__(self, name, hp, atk, **kwargs):
        self.name = name
        self.hp = hp
        self.atk = atk
        print(self.name, "has", self.hp, "hp and", self.atk, "atk!")
        #! Inheritance Fish class, put the parent class in the parameter, this is the new way but its super confusing, dont need below line if use old way
        super().__init__(**kwargs)
        
    def attack(self, target):
        target.hp -= self.atk
        print(self.name, "attacks", target.name, "for", self.atk, "damage!")
        print(target.name, "has", target.hp, "hp left!")
    
    def is_alive(self):
        return self.hp > 0
    
class fish:
    def __init__(self, name, speed, has_scales):
        self.name = name
        self.speed = speed
        self.has_scales = has_scales
        
    def swim(self):
        print(self.name, "swims at", self.speed, "mph!")
        
class shark(monster, fish):
    def __init__(self, sname, shp, satk, sspeed, has_scales, bite_strength):
        #! This is the old way to call parent class attributes
        #monster.__init__(self, name=sname, hp=shp, atk=satk)
        #fish.__init__(self, name=sname, speed=sspeed, has_scales=True)
        #! This is the new way to call parent class attributes
        super().__init__(name, hp, atk)
        
        self.bite_strength = bite_strength
        
    def set_bite_strength(self, bite_strength):
        self.bite_strength = bite_strength
        
#! mro = method resolution order
shark.mro()
# %%

#! Notation for class
class Car:
    #! this is to doctring the class
    """This is a car class"""
    
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

