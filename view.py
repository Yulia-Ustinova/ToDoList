from tabulate import tabulate

class TodoView:
    """Интерфейс для работы с пользователем (View)"""

    def __init__(self):
        pass

    def show_list(self, tasks):
        """метод, выводящий список задач"""
        if tasks:
            list_of_dict = []
            for a in tasks:
                list_of_dict.append(a.__dict__.values())
            print(tabulate(list_of_dict,
                           headers=["№", "Название", "Описание", "Категория", "Приоритет", "Статус"],
                           tablefmt="simple_outline"))
        else:
            print("\nНет задач в списке\n")

    def ask_for_new_task(self):
        """метод, добавляющий задачу в список"""
        name_task = input("Введите название задачи: ")
        description_task = input("Введите описание задачи: ")
        category_task = input("Введите категорию задачи: ")
        priority_task = input("Введите приоритет задачи: ")
        return name_task, description_task, category_task, priority_task

    def ask_for_completed(self):
        """метод, запрашивающий номер для задачи, кот. нужно отметить выполненной"""
        # todo добавить изменение статуса на "Невыполнено"
        return int(input("Введите номер задачи: "))

    def respond_for_completed(self, result, number):
        """метод, сообщающий пользователю, изменен ли статус задачи на 'Выполнена'"""
        if result == 1:
            print(f"\nСтатус задачи №{number} изменен на 'Выполнено'\n")
        else:
            print("\nНомер не найден\n")

    def ask_for_not_completed(self):
        """метод, запрашивающий номер для задачи, кот. нужно отметить НЕвыполненной"""
        return int(input("Введите номер задачи: "))

    def respond_for_not_completed(self, result, number):
        """метод, сообщающий пользователю, изменен ли статус задачи на 'Не выполнена'"""
        if result == 1:
            print(f"\nСтатус задачи №{number} изменен на 'Не выполнено'\n")
        else:
            print("\nНомер не найден\n")

    def ask_for_delete(self):
        """метод, удаляющий задачу из списка"""
        return int(input("Введите номер задачи: "))

    def respond_for_delete(self, result, number):
        """метод, сообщающий пользователю, удалена ли задача"""
        if result == 1:
            print(f"\nЗадача №{number} успешно удалена из списка\n")
        else:
            print("\nНомер не найден\n")

    def get_menu_item(self):
        print("Что вы хотите сделать?")
        print("1. Показать список задач")
        print("2. Добавить задачу в список")
        print("3. Отметить задачу выполненной")
        print("4. Отметить задачу невыполненной")
        print("5. Удалить задачу из списка")
        print("6. Закончить")
        return input("Введите номер пункта, который хотите выполнить: ")
