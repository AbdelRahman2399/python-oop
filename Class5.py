# Composition

class Book:

    def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price
            self.chapters =  {}
            self.count = 0

    def addchapter(self, chapter, pagecount):
        self.chapters[chapter]=pagecount
    
    def Bookpagecount(self):
        pcs= list(self.chapters.values())
        for pc in set(pcs):
            self.count = self.count + pc
        return self.count


    
    def bookname(self):
        print(f'{self.title}')

    def authorname(self):
        print(self.author)

    def prices(self):
            return self.price

class Author:
    def __init__(self,lname):
        #self.fname=fname
        self.lname=lname
        #self.name=(lname,fname)
    def __str__(self):
        return f'{self.lname}'

class Chapter:
    def __init__(self, name, pagecount):
        self.name=name
        self.pagecount=pagecount
        

a1 = Author('Rowling')
c1 = Chapter('Ch1',150)
c2 = Chapter('Ch2',200)
b1 = Book('HP',a1,200)
b1.authorname()
b1.addchapter(c1.name,c1.pagecount)
b1.addchapter(c2.name,c2.pagecount)
print(b1.Bookpagecount())