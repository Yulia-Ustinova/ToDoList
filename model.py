class Task:
    """каждая отдельная задача Task"""
    def __init__(self, number, name, description, category, priority):
        self.number = number
        self.name = name
        self.description = description
        self.category = category
        self.priority = priority
        self.status = "Не выполнено"


class TodoList:
    """хранит список задач (Model)"""

    def __init__(self):
        self.tasks = [Task(1, "Закончить Python задачу", "Пройтись по todo-заметкам и откорректировать мелочи", "Рабочая", "Высокий")]

    def get_list(self):
        """метод для получения списка задач"""
        return self.tasks

    def add_to_list(self, name, description, category, priority):
        """метод, добавляющий задачу в список"""
        new_number = self.create_new_number()
        new_task = Task(new_number, name, description, category, priority)
        self.tasks.append(new_task)

    def create_new_number(self):
        """метод для создания нового номера для новой задачи"""
        if self.tasks:
            last_task = self.tasks[-1]
            last_number = last_task.number
        else:
            last_number = 0
        new_number = last_number + 1
        return new_number

    def mark_complete(self, number):
        """метод, отмечающий выполнение задачи"""
        for a in self.tasks:
            if a.number == number:
                a.status = "Выполнено"
                return 1
        return 0

    def mark_not_complete(self, number):
        """метод, отмечающий задачу невыполненной"""
        for a in self.tasks:
            if a.number == number:
                a.status = "Не выполнено"
                return 1
        return 0

    def delete_task(self, number):
        """метод, удаляющий задачу из списка"""
        for a in self.tasks:
            if a.number == number:
                self.tasks.remove(a)
                return 1
        return 0

