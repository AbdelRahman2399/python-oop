#!/usr/bin/env python3


class Book:
    BookTypes = ('Softcopy','Hardcopy')
    __booklist = None
    def __init__(self, title, booktype, author, price):
        if (booktype in Book.BookTypes):
            self.title = title
            self.booktype = booktype
            self.author = author
            self.price = price
        else:
            print(f'Book Type of {self} not available')
            pass
    
    def bookname(self):
        print(f'{self.title}')

    def authorname(self):
        print(f'{self.author}')

    def prices(self):
        if hasattr(self, '_newprice'):
            return self._newprice
        else:
            return self.price

    def discount(self, disc):
        self._newprice = self.price * disc

    @classmethod
    def getBooktypes(cls):
        return cls.BookTypes

    @staticmethod
    def getBookList():
        if Book.__booklist == None :
            Book.__booklist = []
        
        return Book.__booklist
        

print('Book types:', Book.getBooktypes())
b1 = Book('Harry Potter','Softcopy', 'J.K.Rowling' , 200)
b2 = Book('Harry Potter 2','Hardcopy', 'J.K.Rowling' , 300)
b2.bookname()
#print(b1.prices())
#b1.discount(0.5)
#print(type(b1))
#print(isinstance(b1, Book))
thebooks= Book.getBookList()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)