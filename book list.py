
class Book:
    def __init__(self, title, pages, number, genre):
        self.title = title
        self.pages = pages
        self.number = number
        self.genre = genre

book1 = Book("Harry Potter and the Phisolopher's Stone", 223, "1st", "fantasy")
book2 = Book("Harry Potter and the Chamber of Secrets", 251, "2nd", "fantasy")
book3 = Book("Harry Potter and the Prisoner of Azkaban", 317, "3rd", "fantasy")
book4 = Book("Harry Potter and the Goblet of Fire", 636, "4th", "fantasy")
book5 = Book("Harry Potter and the Order of the Phoenix", 766, "5th", "fantasy")
book6 = Book("Harry Potter and the Half-Blood Prince", 607, "6th", "fantasy")
book7 = Book("Harry Potter and the Deathly Hallows", 607, "7th", "fantasy")

print(f"{book1.title} has {book1.pages}.")
print(f"{book1.title} it's the {book1.number} in the series.")

