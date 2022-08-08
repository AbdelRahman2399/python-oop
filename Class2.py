#Inheritance

class Publication:

    def __init__(self, title, price):
        self.title=title
        self.price=price



class Book(Publication):
    
    def __init__(self, title, author, price):
        super().__init__(title, price)
        self.author = author
        

class Magazine(Publication):
    
    def __init__(self, title, publisher, price):

        super().__init__(title, price)
        self.publisher = publisher

class Newspaper(Magazine):
    
    def __init__(self, title, publisher, price):
        super().__init__(title, publisher,price)

    def TitleInfo(self):
        return self.title


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

N1 = Newspaper('Ahram','Egy', 2)
print(N1.TitleInfo())