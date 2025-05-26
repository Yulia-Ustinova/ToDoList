from tabulate import tabulate

class TodoView:
    """Интерфейс для работы с пользователем (View)"""

    def __init__(self):
        pass

    def show_list(self, tasks: dict) -> None:
        """метод, выводящий список задач"""
        if tasks:
            # переменная list_of_list содержит список списков значений для печати таблицы
            # [
            #     [1, "моя задачка 1","сделать классно", "рабочая", "высокий", "в работе"],
            #     [2, "моя задачка 2","сделать супер", "не рабочая", "низкий", "выполнено"],
            # ]
            list_of_list = []
            task_ids = tasks.keys()
            for id in task_ids:
                # получаем список значений из класса
                list_of_values = list(tasks[id].__dict__.values())
                # вставляем в начало списка значений id
                list_of_values.insert(0, id)
                list_of_list.append(list_of_values)

            print(tabulate(list_of_list,
                           headers=["№", "Название", "Описание", "Категория", "Приоритет", "Статус"],
                           tablefmt="simple_outline"))

        else:
            print("\nНет задач в списке\n")

    def ask_for_new_task(self) -> tuple:
        """метод, добавляющий задачу в список"""
        name_task = input("Введите название задачи: ")
        description_task = input("Введите описание задачи: ")
        category_task = input("Введите категорию задачи: ")
        priority_task = input("Введите приоритет задачи: ")
        return name_task, description_task, category_task, priority_task

    def ask_for_completed(self) -> int:
        """метод, запрашивающий номер для задачи, кот. нужно отметить выполненной"""
        return int(input("Введите номер задачи: "))

    def respond_for_completed(self, result: int, id: int) -> None:
        """метод, сообщающий пользователю, изменен ли статус задачи на 'Выполнена'"""
        if result == 1:
            print(f"\nСтатус задачи №{id} изменен на 'Выполнено'\n")
        else:
            print("\nНомер не найден\n")

    def ask_for_not_completed(self) -> int:
        """метод, запрашивающий номер для задачи, кот. нужно отметить НЕвыполненной"""
        return int(input("Введите номер задачи: "))

    def respond_for_not_completed(self, result: int, id: int) -> None:
        """метод, сообщающий пользователю, изменен ли статус задачи на 'Не выполнена'"""
        if result == 1:
            print(f"\nСтатус задачи №{id} изменен на 'Не выполнено'\n")
        else:
            print("\nНомер не найден\n")

    def ask_for_delete(self) -> int:
        """метод, удаляющий задачу из списка"""
        return int(input("Введите номер задачи: "))

    def respond_for_delete(self, result: int, id: int) -> None:
        """метод, сообщающий пользователю, удалена ли задача"""
        if result == 1:
            print(f"\nЗадача №{id} успешно удалена из списка\n")
        else:
            print("\nНомер не найден\n")

    def get_menu_item(self) -> int:
        print("Что вы хотите сделать?")
        print("1. Показать список задач")
        print("2. Добавить задачу в список")
        print("3. Отметить задачу выполненной")
        print("4. Отметить задачу невыполненной")
        print("5. Удалить задачу из списка")
        print("6. Закончить")
        return int(input("Введите номер пункта, который хотите выполнить: "))
