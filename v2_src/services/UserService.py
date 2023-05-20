import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.User import User
from repository.UserRepository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def authenticate(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and user.password == password:  # this would ideally involve secure password hashing
            return user
        return None

    def register_user(self, username, password, name):
        return self.user_repository.create_user(username, password, name)

if __name__ == '__main__':

    user_service = UserService()
    user_service.user_repository.delete_user('test_username')

    # Test user registration
    new_user = user_service.register_user('test_username', 'test_password', 'Test User')
    assert new_user is not None
    assert new_user.username == 'test_username'
    assert new_user.password == 'test_password'
    assert new_user.name == 'Test User'

    # Test user authentication
    authenticated_user = user_service.authenticate('test_username', 'test_password')
    assert authenticated_user is not None
    assert authenticated_user.username == 'test_username'

    # Cleanup after testing
    user_service.user_repository.delete_user('test_username')
    print("Succesful UserService.py Test!")

 
