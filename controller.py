class TodoController:
    """связывает TodoView и TodoList"""

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self) -> None:
        while True:
            menu_item = self.view.get_menu_item()

            if menu_item == 1:
                self.view.show_list(self.model.get_list())

            elif menu_item == 2:
                name_task, description_task, category_task, priority_task = self.view.ask_for_new_task()
                self.model.add_to_list(name_task, description_task, category_task, priority_task)

            elif menu_item == 3:
                id = self.view.ask_for_completed()
                result = self.model.mark_complete(id)
                self.view.respond_for_completed(result, id)

            elif menu_item == 4:
                id = self.view.ask_for_not_completed()
                result = self.model.mark_not_complete(id)
                self.view.respond_for_not_completed(result, id)

            elif menu_item == 5:
                id = self.view.ask_for_delete()
                result = self.model.delete_task(id)
                self.view.respond_for_delete(result, id)

            elif menu_item == 6:
                break

            else:
                print("Введите корректный номер из списка меню")
