# === 0. Book Class Magic Methods ===
from book_class import Book as MagicBook

# === 1. Library System with Inheritance & Composition ===
from library_system import Book as LibBook, EBook, PrintBook, Library

# === 2. Polymorphism Demo ===
from polymorphism_demo import Rectangle, Circle

# === 3. Class vs Static Methods ===
from class_static_methods_demo import Calculator


def test_magic_methods():
    print("\n--- Magic Methods Test ---")
    my_book = MagicBook("1984", "George Orwell", 1949)
    print(my_book)             # __str__
    print(repr(my_book))       # __repr__
    del my_book                # __del__ will be printed after object is deleted


def test_inheritance_composition():
    print("\n--- Inheritance and Composition Test ---")
    my_library = Library()

    classic_book = LibBook("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()


def test_polymorphism():
    print("\n--- Polymorphism Test ---")
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


def test_class_static_methods():
    print("\n--- Class and Static Methods Test ---")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    test_magic_methods()
    test_inheritance_composition()
    test_polymorphism()
    test_class_static_methods()
