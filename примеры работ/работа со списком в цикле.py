
answer = None
tasks = []


print(
"""
1 - вывести список
2 - добавить задачу
3 - удалить последнюю задачу
4 - очистить список
5 - выйти из программы
6 - всего задач
"""
)

while True:

    try:
        answer = int(input("Напишите цифру от 1 до 5: "))
    except ValueError:
        print("Ввёл неверные данные! Попробуй ещё раз")
        continue

    if answer == 1:
        print(tasks) # выводит переданный элемент
    elif answer == 2:
        new_task = input("Введите новую задачу: ")
        tasks.append(new_task) # добавляет элемент
    elif answer == 3:
        tasks.pop() # удаляет последний элемент
    elif answer == 4:
        tasks.clear() # удаляет весь список
    elif answer == 5:
        break # выходит из цикла
    elif answer == 6:
        print(  f"Количество: {len(tasks)}"   ) # функция len() возвращает количество элементов в списке
    else:
        print("Неверный ответ")



















