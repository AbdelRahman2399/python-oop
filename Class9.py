#Callable Objects


class Book:

    def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price
            self.discount = 0.7

    def __str__(self):
        return f'{self.title} by {self.author} for {self.price}'

    def __call__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price
            self.discount = 0.7 

b1 = Book('Harry Potter','J.K.Rowling',300.0)
print(b1)
b1('The DaVinci Code', 'Dan Brown', 200.0)
print(b1)