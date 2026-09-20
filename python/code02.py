import time
from dataclasses import dataclass,field
from functools import wraps


def time_count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"耗时：{end-start}")
        return func(*args, **kwargs)
    return wrapper

@time_count
def write(num):
    """从1打印到num"""
    for i in range(num):
        print(i+1)


print(write.__name__)
print(write.__doc__)

write(10)


@time_count
def multipy(a:int,b:int):
    """两数相乘"""
    return a*b

print(multipy.__name__)
print(multipy.__doc__)
print(multipy.__annotations__)

print(multipy(8, 9))


##### 对象 ####
#### 类和实例 ####

class student:
    species = "human"
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"hello,my name is {self.name} and I am {self.age} years old")

Tim = student("Tim",20)
Mike = student("Mike",20)

Tim.say_hello()
Mike.say_hello()

print(Tim.species)
print(Mike.species)
print(student.species)


##### 类方法 #####
#
# class User:
#     count = 0
#     def __init__(self,name:str):
#         self.name = name
#         User.count += 1
#
#     ## 普通方法
#     def say_hello(self):
#         return f"hello,my name is {self.name}"
#
#     ## 类方法不需要实例
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     @staticmethod
#     def is_valid_name(name):
#         return len(name) > 2


#### 数据模型和魔术方法
# class User:
#     def __init__(self,name:str,age:int):
#         self.name = name
#         self.age = age
#
#     def __eq__(self,other):
#         return self.age == other.age and self.name == other.name
#
#     def __repr__(self):
#         return f"User(name={self.name!r},age={self.age})"
#
# a = User("Tom",20)
# b = User("Tom",20)
# print(a)
# print(b)
#
# print(a == b)
# print(a is b)
#
# print(repr(a))

# @dataclass
# class User:
#     name:str
#     age:int =20
#
# u1 = User("Tim")
# u2 = User("Tim")
#
# print(u1)
# print(u2)
# print(u1 == u2)

@dataclass
class Product:
    name:str
    price:float

    def discount(self,rate):
        return self.price*(1-rate)

p = Product("macbook",10000)
print(p.discount(0.8))



# 可变对象
@dataclass
class team:
    id:int
    people_list:list[str] = field(default_factory=list)

team1 = team(1,["mike","xiaomai"])
team2 = team(2,["xue","xiaolin"])
print(team1.people_list)
print(team2.people_list)


@dataclass
class Book:
    title:str
    author:str
    price:float=0

    def discount(self,rate):
        return self.price*(1-rate)

book = Book("论语","孔子",59.9)
print(book)
print(book.discount(0.8))