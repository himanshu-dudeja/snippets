# Example for Duck-Typing

# We Assume that if an object walks like a duck and quacks like a duck then its a duck.
# Meaning we don't care what type of object we are working with, we care if our object can do what we ask to do.

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')

class Persons:

    def quack(self):
        print("I'm Quacking like a duck!")

    def fly(self):
        print("I'm flapping my Arms!!")


# Non Duck-Typed(Non-Pythonic)
def non_duck_typed():
    def quack_and_fly(thing):
        if isinstance(thing, Duck):
            thing.quack()
            thing.fly()
        else:
            print('This has to be Duck!')
        print()
    d = Duck()
    quack_and_fly(d)

    p = Persons()
    quack_and_fly(p)


# non_duck_typed()


# Duck-typed(Pythonic)
# We don't care if its a certain type of object we only care if it can do what we ask
def duck_typed():
    def quack_and_fly(thing):
        thing.quack()
        thing.fly()
        print()

    d = Duck()
    quack_and_fly(d)

    p = Persons()
    quack_and_fly(p)


# duck_typed()


# LBYL - Look Before you lead (Non-pythonic)
def lbyl():
    def quack_and_fly(thing):
        if hasattr(thing, 'quack'):
            if callable(thing.quack):
                thing.quack()
        if hasattr(thing, 'fly'):
            if callable(thing.fly):
                thing.fly()
        print()

    d = Duck()
    quack_and_fly(d)

    p = Persons()
    quack_and_fly(p)


# lbyl()


# EAFP - Easier to Ask Forgiveness Permission
def eafp():
    def quack_and_fly(thing):
        try:
            thing.quack()
            thing.fly()
            thing.bark()
        except AttributeError as e:
            print(e)
        print()

    d = Duck()
    quack_and_fly(d)

    p = Persons()
    quack_and_fly(p)


eafp()
