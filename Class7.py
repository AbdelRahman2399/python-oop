#Equality&Comparison

class Book:

    def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

    def __str__(self):
        return f'{self.title} by {self.author} for {self.price}'

    def __eq__(self, value): #check for equality
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare')
        return (self.title == value.title and self.author == value.author and self.price == value.price)

    def __ge__(self, value): #greater than or equal
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare')
        return self.price >= value.price    

    def __lt__(self, value): #less than
        if not isinstance(value, Book):
            raise ValueError('Can\'t compare')
        return self.price < value.price



b1 = Book('Harry Potter','J.K.Rowling',300)
b2 = Book('Harry Potter2','J.K.Rowling',200)
b3 = Book('Harry Potter3','J.K.Rowling',100)
print(b1 == b2)
#print(b1 == b3)
print(b1>=b2)
print(b1<b2)
books = [b2, b1, b3]
books.sort()

for book in books:
    print(book.title)