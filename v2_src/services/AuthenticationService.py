import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from repository.UserRepository import UserRepository
from models.User import User

class AuthenticationService:
    def __init__(self):
        self.user_repo = UserRepository()

    def register_user(self, username, password, name):
        # Check if username already exists
        if self.user_repo.get_user_by_username(username) is not None:
            return False  # Username is taken

        # Create a new user
        user = User(username, password, name)

        # Save the user to the database
        user.set_id(self.user_repo.create_user(user.username, user.password, user.name))

        return True  # Registration successful


    def login_user(self, username, password):
        # Fetch the user by username
        user = self.user_repo.get_user_by_username(username)

        # Check if the user exists and the password is correct
        if user is not None and user.check_password(password):
            return user  # Login successful

        return None  # Login failed

if __name__ == '__main__':
    auth_service = AuthenticationService()
    user_repository = UserRepository()

    user_repository.delete_user('test_username')

    # Testing the creation of a new user
    assert auth_service.register_user("test_username", "test_password", "Test Name") == True, "New user should be successfully registered."

    # Testing registration with an existing username
    assert auth_service.register_user("test_username", "test_password", "Test Name") == False, "Registration should fail if the username already exists."

    # auth_service = AuthenticationService()

    # Testing login with correct username and password
    user = auth_service.login_user("test_username", "test_password")
    assert user is not None, "Login should be successful with correct username and password."
    assert user.username == "test_username", "Logged in user's username should match input."

    # Testing login with incorrect password
    assert auth_service.login_user("test_username", "wrong_password") is None, "Login should fail with incorrect password."

    # Testing login with non-existing username
    assert auth_service.login_user("nonexistent_username", "test_password") is None, "Login should fail with non-existing username."

    user_repository.delete_user('test_username')


    print("AuthenticationService.py Tests Passed!")
