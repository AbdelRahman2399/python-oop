#Attribute Access

class Book:

    def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price
            self.discount = 0.7

    def __str__(self):
        return f'{self.title} by {self.author} for {self.price}'

    def __getattribute__(self, name):
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('discount')
            return p*d
        return super().__getattribute__(name)

    def __setattr__(self, name , value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError('Price must be float')
        return super().__setattr__(name, value)

    def __getattr__(self,name):
        return f'{name} doesn\'t exist'


b1 = Book('Harry Potter','J.K.Rowling',300.0)
print(b1)
print(b1.pizza)