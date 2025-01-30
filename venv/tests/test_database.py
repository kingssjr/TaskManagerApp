import unittest
from app.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")  # Banco de dados em memória

    def test_user_table_exists(self):
        cursor = self.db.get_connection().cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertIsNotNone(cursor.fetchone())