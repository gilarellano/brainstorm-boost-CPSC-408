"""
Member.py

The Member class represents a group member in the BrainstormBoost application. 
Each member is characterized by their name, list of skills, and list of interests. 
The class provides methods to add a new interest or skill to a member.
"""

class Member:
    # Constructor
    def __init__(self, name="", skills=None, interests=None):
        self.name = name
        self.skills = skills if skills else []
        self.interests = interests if interests else []

    def __eq__(self, Member2):
        return self.name == Member2.name

    # Adds an interest to the member's interests
    def AddInterest(self, interest): 
        self.interests.append(str(interest))

    # Adds a skill to the member's skills
    def AddSkill(self, skill):
        self.skills.append(str(skill))

if __name__ == '__main__':
    # Test Member class
    print("Testing Member class...")
    member1 = Member("Luis Rivas", ["Programming", "Data Analysis"], ["Reading", "Cooking"])
    print("Name: ", member1.name)
    print("Interests: ", member1.interests)
    print("Skills: ", member1.skills)

    member1.AddInterest("Hiking")
    member1.AddSkill("Machine Learning")
    print("After adding interest and skill:")
    print("Interests: ", member1.interests)
    print("Skills: ", member1.skills)