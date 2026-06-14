'''__len__ - Define behaviour for  len()
This method allows objects of your class to work with built-in len() function. It should remain the "length" of the
(howver you define that).'''

class Book :
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages
    
b = Book("Python 101",250)
print(len(b))
