class Book:
    title="Fikir Eske Mekabir"
    price=100
    def __init__(self, author):
        self.author = author  
    def property(self):
        print("This is most known book in Ethiopia")

class Book2(Book):
    def another(self):
        print("Author name : ", self.author," WIth price of ", self.price)

b2 = Book2("Haddis Alemayehu")
print(b2.another())