class Library():
    def __init__(self):
        self.books = []
        self.final = []
    
    def add(self, book):
        self.books.append(book)    
    
    def remove(self,book):
        if book in self.books:
            self.books.remove(book)
    
    def search(self, tosearch):
        results = []
        
        for book in self.books:
            if tosearch.lower() in book.lower():
                results.append(book)
        
    def show(self):
        self.final = []
        for i in self.books:
            self.final.append(i)
        print(self.final)
            

mylib = Library()
mylib.add("hairy potter")
mylib.add("tuchel")
mylib.show()
mylib.remove("tuchel")
mylib.show()
    