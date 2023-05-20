create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL
);
"""

create_groups_table = """
CREATE TABLE IF NOT EXISTS group_info (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
"""

create_interests_table = """
CREATE TABLE IF NOT EXISTS interests (
    interest_id INT AUTO_INCREMENT PRIMARY KEY,
    interest_name VARCHAR(255) NOT NULL UNIQUE
);
"""

create_skills_table = """
CREATE TABLE IF NOT EXISTS skills (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(255) NOT NULL UNIQUE
);
"""

create_members_table = """
CREATE TABLE IF NOT EXISTS members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT,
    name VARCHAR(255) NOT NULL,
    skill_id INT,
    interest_id INT,
    FOREIGN KEY (group_id) REFERENCES group_info(group_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id),
    FOREIGN KEY (interest_id) REFERENCES interests(interest_id)
);
"""

create_ideas_table = """
CREATE TABLE IF NOT EXISTS ideas (
    idea_id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (group_id) REFERENCES group_info(group_id)
);
"""

create_votes_table = """
CREATE TABLE IF NOT EXISTS votes (
    vote_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    idea_id INT,
    points INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (idea_id) REFERENCES ideas(idea_id)
);
"""

tables = [
    create_users_table,
    create_groups_table,
    create_interests_table,
    create_skills_table,
    create_members_table,
    create_ideas_table,
    create_votes_table
]