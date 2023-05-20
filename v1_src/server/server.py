from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from Generator import Generator
from Group import Group
from Member import Member
from VotingSystem import VotingSystem
import mysql.connector

# Connect to your MySQL database
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "BrainstormBoost"
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()
print("Succesful db connection!")

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key_here'
Session(app)

generator = None
voting_system = None

# Login API route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Write your SQL query to authenticate the user
    query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        session['user_id'] = user[0]
        return jsonify({'success': True, 'user_id': user[0]})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})

@app.route('/api/check-auth', methods=['GET'])
def check_auth():
    user_id = session.get('user_id')
    if user_id:
        return jsonify({'success': True, 'user_id': user_id})
    else:
        return jsonify({'success': False})

# Register API route
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    name = data['name']

    # Check if the user already exists
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user:
        return jsonify({'success': False, 'message': 'User already exists'})

    # If the user doesn't exist, insert the new user into the database
    query = "INSERT INTO users (username, password_hash, name) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, name)) # Include 'name' here
    connection.commit()

    return jsonify({'success': True, 'message': 'User registered successfully'})

@app.route('/api/group/create', methods=['POST'])
def create_group():
    data = request.get_json()
    user_id = data['user_id']
    group_name = data['group_name']

    cursor = connection.cursor()
    sql = """
    INSERT INTO group_info (user_id, name)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (user_id, group_name))
    connection.commit()
    group_id = cursor.lastrowid
    cursor.close()

    return jsonify(group_id=group_id)

# Fetch user's groups API route
@app.route('/api/groups', methods=['GET'])
def get_groups():
    cursor = connection.cursor(dictionary=True)
    sql = """
    SELECT group_info.group_id, group_info.name, members.name AS member_name, ideas.title AS winning_idea
    FROM group_info
    JOIN members ON group_info.group_id = members.group_id
    JOIN ideas ON group_info.group_id = ideas.group_id
    WHERE ideas.idea_id IN (SELECT MAX(ideas.idea_id) FROM ideas GROUP BY ideas.group_id)
    ORDER BY group_info.group_id
    """
    cursor.execute(sql)
    groups = cursor.fetchall()
    cursor.close()

    return jsonify(groups=groups)

@app.route('/api/group/<int:group_id>', methods=['GET'])
def get_group(group_id):
    cursor = connection.cursor(dictionary=True)
    sql = """
    SELECT group_info.group_id, group_info.name, members.member_id, members.name AS member_name, skills.skill_name, interests.interest_name
    FROM group_info
    JOIN members ON group_info.group_id = members.group_id
    JOIN skills ON members.skill_id = skills.skill_id
    JOIN interests ON members.interest_id = interests.interest_id
    WHERE group_info.group_id = %s
    """
    cursor.execute(sql, (group_id,))
    members = cursor.fetchall()
    cursor.close()

    return jsonify(members=members)

@app.route('/api/group/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    data = request.get_json()
    members = data['members']

    cursor = connection.cursor()
    for member in members:
        sql = """
        UPDATE members
        SET name=%s, skill_id=%s, interest_id=%s
        WHERE member_id=%s
        """
        cursor.execute(sql, (member['name'], member['skill_id'], member['interest_id'], member['member_id']))
    connection.commit()
    cursor.close()

    return jsonify(success=True)


# Fetch group members API route
@app.route('/api/group/<int:group_id>/members', methods=['GET'])
def get_group_members(group_id):
    # Write your SQL query to fetch group members and their attributes
    query = "SELECT * FROM members WHERE group_id = %s"
    cursor.execute(query, (group_id,))
    members = cursor.fetchall()

    return jsonify([{'member_id': member[0], 'name': member[2], 'skills': member[3], 'interests': member[4]} for member in members])


# Fetch group ideas API route
@app.route('/api/group/<int:group_id>/ideas', methods=['GET'])
def get_group_ideas(group_id):
    # Write your SQL query to fetch group ideas
    query = "SELECT * FROM ideas WHERE group_id = %s"
    cursor.execute(query, (group_id,))
    ideas = cursor.fetchall()

    return jsonify([{'idea_id': idea[0], 'title': idea[2], 'description': idea[3]} for idea in ideas])

# members API route
@app.route('/api/members', methods=['POST'])
def add_members():
    global generator
    global voting_system

    projectDesc = request.get_json()['projectDescription'] # string
    memberInfo = request.get_json()['memberInfo'] # array of dictionaries with member 'name' and 'skills'

    # Create a group with the project description
    group = Group()
    group.projectDesc = projectDesc

    for member_data in memberInfo:
        name = member_data['name']
        skills = member_data['skills'].split(', ')
        interests = member_data['interests'].split(', ')
        member = Member(name, skills, interests)
        group.AddMember(member)

    generator = Generator(group)
    generator.CreatePrompt()
    generator.Generate()
    generator.ParseIdeas()
    ideas = generator.ideas

    # Create a new VotingSystem object with the generator's ideas
    voting_system = VotingSystem(generator)

    return jsonify({'ideas': [{'title': idea.title, 'description': idea.description} for idea in ideas]})

@app.route('/vote', methods=['POST'])
def handle_vote():
    global voting_system

    data = request.json
    votes = data.get('votes')
    numMembers = data.get('numMembers')

    # Cast votes on the current VotingSystem object
    voting_system.CastVote(votes[0], votes[1], votes[2])

    # Display the voting results
    message = voting_system.DisplayWinner()

    return jsonify({'success': True, 'message': message})

if __name__ == "__main__":
    app.run(debug=True)
