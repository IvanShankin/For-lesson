grades = [5, 4, 3, 5, 4, 4, 5, 3]
string_with_grade = ""

for grade in grades:
    string_with_grade += f"{grade}, "

print(string_with_grade)
print(len(grades))
print(sum(grades) / 8)


new_grade = int(input("Введите новое значение: "))

if new_grade >= 1 and new_grade <= 5:
    grades.append(new_grade)
    print()
else:
    print("Ошибка! Оценка должна быть от 1 до 5")

print(f"Количество пятёрок: {grades.count(5)}")
print(f"Количество двоек: {grades.count(2)}")