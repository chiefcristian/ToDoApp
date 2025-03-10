class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f'{self.code_id}-{self.title}'
class TodoBook:
    def __int__(self):
        self.todos = {}
    def add_todo(self, title: str, description: str )-> int:

       code_id = len(self.todos) + 1
       new_todo = Todo(code_id, title,description)
       self.todos[code_id]= new_todo
       return code_id
    def pending_todos(self)-> list[Todo]:
        return [Todo for todo in self.values() if not todo.completed]
    def completed_todos(self)-> list[Todo]:
        return [Todo for todo in self.values() if todo.completed]
    def tangs_todo_count(self)-> dict[str, int]:
        tag_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count
