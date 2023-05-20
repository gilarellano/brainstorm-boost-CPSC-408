import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.queries import create_group, get_group_by_id, delete_group
from db.database import create_db_connection
from repository.UserRepository import *

class GroupRepository:
    def __init__(self):
        self.connection = create_db_connection()

    def create_group(self, user_id, name, description):
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_group, (user_id, name, description))
            self.connection.commit()
            group_id = cursor.lastrowid
            cursor.close()
            return group_id
        except Exception as e:
            print(f"Error occurred while creating group: {e}")
            return None

    def get_group_by_id(self, group_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_group_by_id, (group_id,))
            group = cursor.fetchone()
            cursor.close()
            print("We did get an id from the group: ", group_id)
            return group
        except Exception as e:
            print("We did not get an id from the group")
            print(f"Error occurred while retrieving group: {e}")
            return None

    def delete_group(self, group_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_group, (group_id,))
            self.connection.commit()
            cursor.close()

            return True
        except Exception as e:
            print(f"Error occurred while deleting group: {e}")
            return False

if __name__ == '__main__':
    # Create a GroupRepository instance
    group_repo = GroupRepository()
    user_repo = UserRepository()

    user_repo.delete_user('test_user')
    new_user = user_repo.create_user('test_user', 'test_pass', 'Test Name')

    # Create a new group
    group_id = group_repo.create_group(new_user.user_id, "Test Group", "This is a test group.")
    assert group_id is not None, "Failed to create a new group."

    # Retrieve the group by ID
    group = group_repo.get_group_by_id(group_id)
    assert group is not None, "Failed to retrieve the group by ID."

    # Delete the group
    delete_result = group_repo.delete_group(group_id)
    assert delete_result, "Failed to delete the group."
    #user_repo.delete_user('test_user')

    # Verify that the group is deleted
    group = group_repo.get_group_by_id(group_id)
    assert group is None, "Group still exists after deletion."

    print("GroupRepository test completed.")
