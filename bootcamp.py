class Library:
    def __init__(self):
        self.books = "books.txt"
        self.file = open(self.books,'a+',encoding='utf-8')
        self.menu()
    def __del__(self):
        self.file.close()
        print("library is closed")


    def menu (self):
        while True:
            print(""""MENU
            1)List Books
            2)Add Book
            3)Remove Book
            Q)Quit
            """)
            user = input("choice: ")
            if user == "1":
                self.listbooks()
            elif user == "2":
                self.addbook()
            elif user == "3":
                self.removebook()
            elif user == "q" or user == "Q":
                print("Goodbye")
                break
            else:
                print("please enter a number")

    def addbook(self):
        title = input("book title: ")
        author = input("book author: ")
        year = input("release year: ")
        pages = input("number of pages :")
        string = (f"{title},{author},{year},{pages}\n")
        self.file.seek(0)
        self.file.write(string)

    def removebook(self):
        book_title_to_remove = input("book title to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for book in lines:
            found = book.find(book_title_to_remove)
            if found == 0:
                lines.remove(book)
        self.file.truncate(0)
        for book in lines:
            info = book.split(",")
            string = f"{info[0]},{info[1]},{info[2]},{info[3]}\n"
            self.file.seek(0)
            self.file.write(string)


    def listbooks(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for book in lines:
            info = book.split(",")
            print(f"author: {info[1]}, book name: {info[0]}")




if __name__ == '__main__':
    lib = Library()
    del lib


