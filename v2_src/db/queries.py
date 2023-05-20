
# Query to create a new user
create_user = """
INSERT INTO `users`(username, password, name)
VALUES (%s, %s, %s);
"""

# Query to retrieve user by username
get_user_by_username = """
SELECT * FROM `users` WHERE username = %s;
"""

# Query to create a new group
create_group = """
INSERT INTO `groups`(user_id, name, description)
VALUES (%s, %s, %s);
"""

# Query to retrieve groups by user_id
get_groups_by_user_id = """
SELECT * FROM `groups` WHERE user_id = %s;
"""

# Query to create a new member
create_member = """
INSERT INTO members (group_id, name)
VALUES (%s, %s);
"""

# Query to retrieve members by group_id
get_members_by_group_id = """
SELECT * FROM members WHERE group_id = %s;
"""

# Query to create a new skill
create_skill = """
INSERT INTO skills (skill_name)
VALUES (%s);
"""

# Query to create a new interest
create_interest = """
INSERT INTO interests (interest_name)
VALUES (%s);
"""

# Query to assign a skill to a member
assign_skill_to_member = """
INSERT INTO member_skills (member_id, skill_id)
VALUES (%s, %s);
"""

# Query to assign an interest to a member
assign_interest_to_member = """
INSERT INTO member_interests (member_id, interest_id)
VALUES (%s, %s);
"""

# Query to create a new idea
create_idea = """
INSERT INTO ideas (group_id, title, description)
VALUES (%s, %s, %s);
"""

# Query to retrieve ideas by group_id
get_ideas_by_group_id = """
SELECT * FROM ideas WHERE group_id = %s;
"""

# Query to cast a vote
cast_vote = """
INSERT INTO votes (member_id, idea_id, rank)
VALUES (%s, %s, %s);
"""

# Query to retrieve votes by idea_id
get_votes_by_idea_id = """
SELECT * FROM votes WHERE idea_id = %s;
"""

# Query to retrieve a group by ID
get_group_by_id = """
SELECT * FROM `groups` WHERE group_id = %s;
"""

# Query to delete a group
delete_group = """
DELETE FROM `groups` WHERE group_id = %s;
"""

assign_skill_to_member = """
INSERT INTO member_skills (member_id, skill_id)
VALUES (%s, %s);
"""

assign_interest_to_member = """
INSERT INTO member_interests (member_id, interest_id)
VALUES (%s, %s);
"""

delete_member_skills = """
DELETE FROM member_skills
WHERE member_id = %s;
"""

delete_member_interests = """
DELETE FROM member_interests
WHERE member_id = %s;
"""

delete_member = """
DELETE FROM members
WHERE member_id = %s;
"""

# Query to retrieve a member by ID
get_member_by_id = """
SELECT * FROM `members` WHERE member_id = %s;
"""

# Query to retrieve member skills by member ID
get_member_skills = """
SELECT s.skill_name FROM `skills` s
JOIN `member_skills` ms ON s.skill_id = ms.skill_id
WHERE ms.member_id = %s;
"""

# Query to retrieve member interests by member ID
get_member_interests = """
SELECT i.interest_name FROM `interests` i
JOIN `member_interests` mi ON i.interest_id = mi.interest_id
WHERE mi.member_id = %s;
"""

# Query to add a skill to a member
add_skill_to_member = """
INSERT INTO `member_skills` (member_id, skill_id)
VALUES (%s, %s);
"""

# Query to add an interest to a member
add_interest_to_member = """
INSERT INTO `member_interests` (member_id, interest_id)
VALUES (%s, %s);
"""


def test_user_creation_and_retrieval():
    from database import create_db_connection
    conn = create_db_connection()
    cursor = conn.cursor()

    # Retrieve the id of any existing user with the test username
    cursor.execute(get_user_by_username, ('test_user',))
    user = cursor.fetchone()
    if user is not None:
        user_id = user[0]
        
        # Delete any groups associated with the user
        cursor.execute('DELETE FROM `groups` WHERE user_id = %s;', (user_id,))
        conn.commit()
        
        # Now it's safe to delete the user
        cursor.execute('DELETE FROM `users` WHERE user_id = %s;', (user_id,))
        conn.commit()

    # Create a new user
    cursor.execute(create_user, ('test_user', 'test_password', 'Test User'))
    conn.commit()

    # Retrieve the newly created user
    cursor.execute(get_user_by_username, ('test_user',))
    user = cursor.fetchone()

    assert user[1] == 'test_user'  # Check that the username matches
    assert user[2] == 'test_password'  # Check that the password hash matches
    assert user[3] == 'Test User'  # Check that the name matches

    cursor.close()
    conn.close()
    print("Succesful test_user_creation")



def test_group_creation_and_retrieval():
    from database import create_db_connection
    conn = create_db_connection()
    cursor = conn.cursor()

    # Clean up any existing user with the test username
    cursor.execute('DELETE FROM `users` WHERE username = %s;', ('test_user',))
    conn.commit()


    # Create a new user
    cursor.execute(create_user, ('test_user', 'test_password', 'Test User'))
    conn.commit()

    # Retrieve the newly created user
    cursor.execute(get_user_by_username, ('test_user',))
    user = cursor.fetchone()

    # Clean up any existing user with the test username
    cursor.execute('DELETE FROM `groups` WHERE name = %s;', ('Test Group',))
    conn.commit()

    # Create a new group with the retrieved user_id
    cursor.execute(create_group, (user[0], 'Test Group', 'This is a test group.'))
    conn.commit()

    # Retrieve the newly created group
    cursor.execute(get_groups_by_user_id, (user[0],))
    group = cursor.fetchone()

    assert group[1] == user[0]  # Check that the user_id matches
    assert group[2] == 'Test Group'  # Check that the group name matches
    assert group[3] == 'This is a test group.'  # Check that the description matches

    # Clean up after the test
    cursor.execute('DELETE FROM `groups` WHERE name = %s;', ('Test Group',))
    cursor.execute('DELETE FROM `users` WHERE username = %s;', ('test_user',))
    conn.commit()

    cursor.close()
    conn.close()
    print("Succesful group_user_creation")


if __name__ == '__main__':
    test_user_creation_and_retrieval()
    test_group_creation_and_retrieval()