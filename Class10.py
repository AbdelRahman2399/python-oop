#DataClass/PostInit

from dataclasses import dataclass, field
import random

def page_func():
    return float(random.randrange(2000,4000))


@dataclass
class Book:

    title : str = 'No Title'
    author : str = 'No Name'
    price : int = field(default=10.0)
    pages : int = field(default_factory=page_func)

    def __post_init__(self):
        self.description = f'{self.title} by {self.author}'

    def bookinfo(self):
        return f'{self.title} by {self.author}'

b1 = Book('Harry Potter','J.K.Rowling',300.0)
b2 = Book('The DaVinci Code', 'Dan Brown', 200.0,2000)
print(b1.title)
print(b1)
print(b1==b2)
b1.title = 'Harry Potter 2'
print(b1.bookinfo())
print(b1.description)
b3 = Book()
print(b3)