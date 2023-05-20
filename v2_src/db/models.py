create_users_table = """
CREATE TABLE IF NOT EXISTS `users` (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NOT NULL
);
"""

create_groups_table = """
CREATE TABLE IF NOT EXISTS `groups` (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    `name` VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES `users`(user_id) ON DELETE CASCADE
);
"""

create_members_table = """
CREATE TABLE IF NOT EXISTS `members` (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT,
    `name` VARCHAR(255) NOT NULL,
    FOREIGN KEY (group_id) REFERENCES `groups`(group_id) ON DELETE CASCADE
);
"""

create_interests_table = """
CREATE TABLE IF NOT EXISTS `interests` (
    interest_id INT AUTO_INCREMENT PRIMARY KEY,
    `interest_name` VARCHAR(255) NOT NULL UNIQUE
);
"""

create_skills_table = """
CREATE TABLE IF NOT EXISTS `skills` (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    `skill_name` VARCHAR(255) NOT NULL UNIQUE
);
"""

create_member_interests_table = """
CREATE TABLE IF NOT EXISTS `member_interests` (
    member_id INT,
    interest_id INT,
    PRIMARY KEY (member_id, interest_id),
    FOREIGN KEY (member_id) REFERENCES `members`(member_id) ON DELETE CASCADE,
    FOREIGN KEY (interest_id) REFERENCES `interests`(interest_id) ON DELETE CASCADE
);
"""

create_member_skills_table = """
CREATE TABLE IF NOT EXISTS `member_skills` (
    member_id INT,
    skill_id INT,
    PRIMARY KEY (member_id, skill_id),
    FOREIGN KEY (member_id) REFERENCES `members`(member_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES `skills`(skill_id) ON DELETE CASCADE
);
"""

create_ideas_table = """
CREATE TABLE IF NOT EXISTS `ideas` (
    idea_id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT,
    `title` VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (group_id) REFERENCES `groups`(group_id) ON DELETE CASCADE
);
"""

create_votes_table = """
CREATE TABLE IF NOT EXISTS `votes` (
    vote_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    idea_id INT,
    rank_num INT,
    FOREIGN KEY (member_id) REFERENCES `members`(member_id) ON DELETE CASCADE,
    FOREIGN KEY (idea_id) REFERENCES `ideas`(idea_id) ON DELETE CASCADE
);
"""

tables = [
    create_users_table,
    create_groups_table,
    create_members_table,
    create_interests_table,
    create_skills_table,
    create_member_interests_table,
    create_member_skills_table,
    create_ideas_table,
    create_votes_table
]
