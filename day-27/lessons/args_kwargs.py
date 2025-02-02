# def add(a,b):
#     print(a, b)
# def add(*args):
#     (print(number) for number in args)

def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

print(add(1,2,3,4,5,6))

# ==================================== kwargs - KeyWordArguments - it's basically dictionary
def calculate(n, **kwargs):
    print(type(kwargs))
    # for key,value in kwargs.items():
    #     print(key, value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        ## we can also use .get. This will result in None if user won't provide parameter
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Nissan",model="GT-R")
print(my_car.make, my_car.model, my_car.colour)