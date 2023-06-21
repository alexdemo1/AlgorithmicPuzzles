# todo_list_manager.py

class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {self.description} ({status})"


class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Todo item added.")

    def mark_item_completed(self, item_title):
        for item in self.items:
            if item.title == item_title:
                item.completed = True
                print("Todo item marked as completed.")
                return
        print("Todo item not found.")

    def display_list(self):
        if self.items:
            print("Todo List:")
            for item in self.items:
                print(item)
        else:
            print("Todo list is empty.")

# Usage example
todo_list = TodoList()

item1 = TodoItem("Buy groceries", "Milk, eggs, bread")
item2 = TodoItem("Finish project", "Complete documentation")
item3 = TodoItem("Call John", "Discuss upcoming meeting")

todo_list.add_item(item1)
todo_list.add_item(item2)
todo_list.add_item(item3)

todo_list.display_list()

todo_list.mark_item_completed("Buy groceries")
todo_list.mark_item_completed("Send email")

todo_list.display_list()
