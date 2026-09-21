def add(a:int, b:int) -> int:
    return a+b


# print(add(1, 2))
# print(add("1", "2"))
# print(add([1], [2]))

from collections.abc import Callable
def calculate(
        func: Callable[[int,int], int],
        a: int,
        b: int
)-> int:
    return func(a,b)

from typing import TypeVar,Generic
T = TypeVar('T')

def identity(value:T)->T:
    return value

a = identity(10)
b = identity("hello")
c = identity([1,2,3])

class Box(Generic[T]):
    def __init__(self, value:T):
        self.value = value

    def get(self) -> T:
        return self.value


from typing import Protocol

class Speaker(Protocol):
    def speak(self)->str:
        ...

def make_sound(animal:Speaker)->None:
    print(animal.speak())

class Dog:
    def speak(self)->str:
        return "wang"

class Cat:
    def speak(self)->str:
        return ("miao")

make_sound(Dog())
make_sound(Cat())
