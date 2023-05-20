import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import create_db_connection
from models.User import User

class UserRepository:
    def get_user_by_username(self, username):
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT username, password, name, user_id FROM users WHERE username = %s;", (username,))
        record = cursor.fetchone()
        if record:
            return User(*record)
        return None

    def create_user(self, username, password, name):
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO `users`(username, password, name) VALUES (%s, %s, %s);",
            (username, password, name)
        )
        connection.commit()
        
        return self.get_user_by_username(username)

    def delete_user(self, username):
        connection = create_db_connection()
        cursor = connection.cursor()
        query = 'DELETE FROM `users` WHERE username = %s'
        cursor.execute(query, (username,))
        connection.commit()
        cursor.close()

if __name__ == '__main__':

    user_repository = UserRepository()
    # Remove any previous tests
    user_repository.delete_user('test_username')

    # Test user creation
    new_user = user_repository.create_user('test_username', 'test_password', 'Test User')
    assert new_user is not None
    assert new_user.username == 'test_username'
    assert new_user.password == 'test_password'
    assert new_user.name == 'Test User'

    # Test retrieving a user
    retrieved_user = user_repository.get_user_by_username('test_username')
    assert retrieved_user is not None
    assert retrieved_user.username == 'test_username'

    # Cleanup after testing
    user_repository.delete_user('test_username')
    print("Successful UserRepositor.py Test!")