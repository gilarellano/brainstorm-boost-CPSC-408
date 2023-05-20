import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import create_db_connection
from db.queries import *

class MemberRepository:
    def __init__(self):
        self.connection = create_db_connection()

    def create_member(self, group_id, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_member, (group_id, name))
            self.connection.commit()
            member_id = cursor.lastrowid
            cursor.close()
            return member_id
        except Exception as e:
            print(f"Error occurred while creating member: {e}")
            return None

    def delete_member(self, member_id):
        try:
            self.delete_member_interests(member_id)
            self.delete_member_skills(member_id)

            cursor = self.connection.cursor()
            cursor.execute(delete_member, (member_id,))
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error occurred while deleting member: {e}")

    
    def get_member_by_id(self, member_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_member_by_id, (member_id,))
            record = cursor.fetchone()
            cursor.close()
            if record:
                member = Member(name=record[2])
                return member
            return None
        except Exception as e:
            print(f"Error occurred while retrieving member: {e}")
            return None

    def get_member_skills(self, member_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_member_skills, (member_id,))
            records = cursor.fetchall()
            cursor.close()
            skills = [record[0] for record in records]
            return skills
        except Exception as e:
            print(f"Error occurred while retrieving member skills: {e}")
            return []

    def get_member_interests(self, member_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(get_member_interests, (member_id,))
            records = cursor.fetchall()
            cursor.close()
            interests = [record[0] for record in records]
            return interests
        except Exception as e:
            print(f"Error occurred while retrieving member interests: {e}")
            return []

    def delete_member_interests(self, member_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_member_interests, (member_id,))
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error occurred while deleting member interests: {e}")

    def delete_member_skills(self, member_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_member_skills, (member_id,))
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error occurred while deleting member skills: {e}")

    def add_skill_to_member(self, member_id, skill_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(assign_skill_to_member, (member_id, skill_id))
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error occurred while assigning skill to member: {e}")

    def add_interest_to_member(self, member_id, interest_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(assign_interest_to_member, (member_id, interest_id))
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error occurred while assigning interest to member: {e}")

from repository.MemberRepository import MemberRepository
from repository.GroupRepository import GroupRepository
from repository.UserRepository import UserRepository
from models.Member import Member

if __name__ == '__main__':
    # Create a MemberRepository instance
    member_repo = MemberRepository()
    group_repo = GroupRepository()
    user_repo = UserRepository()

    user_repo.delete_user('test_username')

    new_user = user_repo.create_user('test_username', 'test_password', 'Test Name')

    # Create a new group
    group_id = group_repo.create_group(new_user.user_id, "Test Group", "This is a test group.")
    assert group_id is not None, "Failed to create a new group."

    # Create a new member
    member = Member(name='Test_Member Name')
    member_id = member_repo.create_member(group_id, member.name)
    assert member_id is not None, "Failed to create a new member."

    # Retrieve the member by ID
    retrieved_member = member_repo.get_member_by_id(member_id)
    assert retrieved_member is not None, "Failed to retrieve the member by ID."
    assert retrieved_member.name == member_name, "Retrieved member name does not match."

    # Add skills to the member
    skills = ["Skill 1", "Skill 2", "Skill 3"]
    member_repo.add_skills(member_id, skills)

    # Retrieve the member's skills
    retrieved_skills = member_repo.get_member_skills(member_id)
    assert retrieved_skills == skills, "Retrieved skills do not match the added skills."

    # Add interests to the member
    interests = ["Interest 1", "Interest 2", "Interest 3"]
    member_repo.add_interests(member_id, interests)

    # Retrieve the member's interests
    retrieved_interests = member_repo.get_member_interests(member_id)
    assert retrieved_interests == interests, "Retrieved interests do not match the added interests."

    # Delete the member
    member_repo.delete_member(member_id)

    # Verify that the member is deleted
    deleted_member = member_repo.get_member_by_id(member_id)
    assert deleted_member is None, "Member still exists after deletion."

    print("MemberRepository test completed.")
