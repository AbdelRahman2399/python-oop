#String Representation


class Book:

    def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

    def __str__(self):
        return f'{self.title} by {self.author} for {self.price}'

    def __repr__(self):
        return f'title = {self.title}'

b1 = Book('Harry Potter','J.K.Rowling',200)
print(b1)
print(repr(b1))