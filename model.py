from dataclasses import dataclass

@dataclass
class Task:
    """каждая отдельная задача Task"""
    name: str
    description: str
    category: str
    priority: str
    status: str = "Не выполнено"


class TodoList:
    """хранит список задач (Model)"""

    _last_id = 0

    def __init__(self) -> None:
        self.tasks = {self._create_new_id(): Task("Закончить Python задачу", "Пройтись по todo-заметкам и откорректировать мелочи", "Рабочая", "Высокий")}

    def get_list(self) -> dict:
        """метод для получения списка задач"""
        return self.tasks

    def add_to_list(self, name: str, description: str, category: str, priority: str) -> None:
        """метод, добавляющий задачу в список"""
        new_id = self._create_new_id()
        new_task = Task(name, description, category, priority)
        self.tasks.update({new_id: new_task})

    def _create_new_id(self) -> int:
        """метод для создания нового номера для новой задачи"""
        self._last_id = self._last_id + 1
        return self._last_id

    def mark_complete(self, id: int) -> int:
        """метод, отмечающий выполнение задачи"""
        if id in self.tasks.keys():
            self.tasks[id].status = "Выполнено"
            result = 1
        else:
            result = 0
        return result

    def mark_not_complete(self, id: int) -> int:
        """метод, отмечающий задачу невыполненной"""
        if id in self.tasks.keys():
            self.tasks[id].status = "Не выполнено"
            result = 1
        else:
            result = 0
        return result

    def delete_task(self, id: int) -> int:
        """метод, удаляющий задачу из списка"""
        if id in self.tasks.keys():
            del self.tasks[id]
            result = 1
        else:
            result = 0
        return result

