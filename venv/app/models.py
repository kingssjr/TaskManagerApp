class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Task:
    def __init__(self, user_id, title, description, priority, deadline):
        self.user_id = user_id
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.status = 'Pending'