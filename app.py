# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age + 1
#
#     @staticmethod
#     def asd(cls):
#         print(cls)
#         pass
#
# person1 = Person('Heghine', 28)
# print(person1.name, person1.age)
# print(person1.asd(Person))

#
# class CoffeeShop:
#     specialty = 'espresso'
#     adds = 3
#
#     def __init__(self, coffee_price):
#         self.coffee_price = coffee_price
#
#     @staticmethod
#     def check_weather(price):
#         print('Its sunny')
#         return price + 2
#
#     def make_coffee(self):
#         new_price = CoffeeShop.check_weather(self.coffee_price)
#         print(f'Making {self.specialty} for ${new_price + CoffeeShop.adds}')
#
#     @classmethod
#     def change_specialty(cls, specialty):
#         cls.specialty = specialty
#         print(f'Specialty changed to {specialty}')
#
#
# cofee_shop = CoffeeShop(7)
# cofee_shop.make_coffee()
# cofee_shop.change_specialty('milk coffee')
#
# cofee_shop.make_coffee()
from functools import reduce


# def add_three(x, y):
#     print(x,y)
#     return x + y
#
#
# li = [1, 2, 3, 5]
#
# reduce(add_three, li)

# list = [3,2,1]
#
# print(list[::-1])


# import pickle
# obj = [
#     {'id': 1, 'name': 'Stuffy'},
#     {'id': 2, 'name': 'Fluffy'}
# ]
#
# with open('file.p', 'wb') as f:
#     pickle.dump(obj, f)
# with open('file.p', 'rb') as f:
#     loaded_obj = pickle.load(f)
# print(loaded_obj)


# a = [1,2,3]
#
# b = a
# a.extend([4,5])
# print(a, b)
# print(a is b)

# a = ['a','b','c', 'd']
# b = [1,2,3]
#
# print(tuple(zip(a,b)))
#[(k,v) for k,v in zip(a,b)]


# li = ['a','b','c','d','e']
# for idx,val in enumerate(li):
#     print(idx, val)

# li = [1, 2, 3, 4]
#
# li2 = [i + 1 for i in li if i >= 2]
# print(li2)

#x = 1

# print('greater' if x > 3 else 'less')


# d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
# print(list(d))
# print(list(d.items()))

# creating a list of letters aaa $
b = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
print({ key: value + 1 for key, value in b.items() })

