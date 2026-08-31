books = [
    "Гарри Поттер",
    "Властелин колец",
    "Шерлок Холмс",
    "1984",
    "Маленький принц"
]

string_with_books = ""
for book in books:
    string_with_books += f"{book}, "

print(string_with_books)
print(len(books))

new_book = input("Введите название книги: ")
if new_book != "":
    books.append(new_book)
    print("Книга добавлена!")
else:
    print("Ошибка! Название книги не может быть пустым")


first_book = books[0]
print(books.count(first_book))