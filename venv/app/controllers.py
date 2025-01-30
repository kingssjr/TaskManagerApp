from app.database import Database
from app.utils import hash_password, verify_password

class TaskManagerController:
    def __init__(self):
        self.db = Database()

    def register(self, username, password):
        cursor = self.db.get_connection().cursor()
        try:
            hashed_password = hash_password(password)
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.db.get_connection().commit()
            return True
        except Exception as e:
            print("Error during registration:", e)
            return False

    def login(self, username, password):
        cursor = self.db.get_connection().cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result and verify_password(password, result[0]):
            return True
        return False