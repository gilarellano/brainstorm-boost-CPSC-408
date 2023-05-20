"""
Group.py

The Group class represents a project group in the BrainstormBoost application. 
Each group is characterized by its project description and a list of members. 
The class provides methods to add a new member to the group or remove an existing member.
"""

class Group:
    # Init class
    def __init__(self, projectDesc="", members=None):
        self.projectDesc = projectDesc
        self.members = members if members else []

    # Adds member to the member array
    def AddMember(self, newMember):
        self.members.append(newMember)

    # Removes a member from the group
    def RemoveMember(self, memberPos):
        try:
            del self.members[memberPos]
        except IndexError:
            return -1

if __name__ == '__main__':

    from Member import Member
    # Test Group class
    print("\nTesting Group class...")
    member1 = Member("John Doe", ["C++", "Data Structures"], ["Video Games", "Reading"])
    member2 = Member("Jane Doe", ["Web Design", "UX/UI"], ["Photography", "Travelling"])
    
    group1 = Group("AI project", [member1])
    print("Group's Project:", group1.projectDesc)
    print("Group's Members:", len(group1.members))

    group1.AddMember(member2)
    print("After adding a member:")
    print("Group's Members:", len(group1.members))

    for member in group1.members:
        print("Name: ", member.name)
