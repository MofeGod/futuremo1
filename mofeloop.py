book_in_library = ["Faith", "Hope", "Charity", "precepts", "understanding", "life"]

def view_books():  
    print(f"here are the available books: {book_in_library}")   
   
def borrow_book():
    book_to_borrow = input("which book would you like to borrow: ").casefold()
    
    if book_to_borrow not in book_in_library:
               print("this book is not availabe")
               print(f"here are the available books: {book_in_library}")

    else:
        for book in book_in_library:
            if book_to_borrow == book:
                book_in_library.remove(book_to_borrow)
        print(f"you borrowed {book_to_borrow}")
    
    
def return_book():
    book_to_return = input("which book would you like to return: ").casefold()
    book_in_library.append(book_to_return)
    print(f"you have returned {book_to_return} to the library")


print("""Welcome!
type:
'view' to view books
'borrow' to borrow books
'return' to return books
 'quit'  to exit""")

while True:
    operation =  input("what would you like to do at the library today:").casefold()
    if operation == "view":
                        view_books()

    elif operation == "borrow":
                        borrow_book()

    elif operation == "return":
                        return_book()
    
    elif operation == "quit": 
                print("good bye!!!") 
                break
    else:
                print('invalid operation.')
