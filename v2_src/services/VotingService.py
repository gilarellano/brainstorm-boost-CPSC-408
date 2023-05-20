import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.GeneratorService import Generator
from models.Member import Member
from models.Group import Group

class VotingSystem:
    # Init class
    # ideas is a list of Idea objects passed in from Generator
    def __init__(self, generator):
        self.generator = generator
        self.votes = [0] * len(generator.ideas)

    def DisplayIdeas(self):
        for index, idea in enumerate(self.generator.ideas, start=1):
            print(f"{index}. {idea.title}")
            print(idea.description)
            print()

    def CastVote(self, first_choice, second_choice, third_choice):
        choices = [first_choice, second_choice, third_choice]
        for index, choice in enumerate(choices, start=1):
            if 1 <= choice <= len(self.votes):
                self.votes[choice - 1] += (4 - index)  # Assign 3 points for 1st choice, 2 points for 2nd choice, 1 point for 3rd choice
            else:
                print(f"Invalid idea index for choice {index}. Please try again.")

    def DisplayResults(self):
        print("\nVoting Results:")
        for index, idea in enumerate(self.generator.ideas, start=1):
            print(f"{index}. {idea.title} - {self.votes[index - 1]} votes")

    def DisplayWinner(self):
        winner_index = self.votes.index(max(self.votes))
        winning_idea = self.generator.ideas[winner_index]
        print("\nWinning Idea:")
        print(f"{winner_index + 1}. {winning_idea}")
        return(f"{winner_index + 1}. {winning_idea}")

if __name__ == "__main__":
    # Create a test Group
    testGroup = Group("Software Development Project")
    testGroup.projectDesc = "Develop a software application in a team"
    testGroup.AddMember(Member("Alice", ["Python", "Data Structures"], ["Video Games", "Running"]))
    testGroup.AddMember(Member("Bob", ["Web Design"], ["Cooking", "Music"]))
    testGroup.AddMember(Member("Charlie", ["C++", "Data Structures"], ["Video Games", "Soccer"]))

    # Create a test Generator
    testGenerator = Generator(testGroup)
    testGenerator.CreatePrompt()

    # Mock response for the generator
    testGenerator.response = '''
1. Game Development Project: Develop a video game using Python. Alice can use her Python skills and Charlie can use his C++ skills for game logic, while Bob can design the game interface.

2. Music Application: Develop a music streaming app. Alice can handle the back-end with Python, Bob can design the user interface, and Charlie can help with additional programming in C++.

3. Cooking Recipe Website: Create a website for sharing and discovering new cooking recipes. Bob can take the lead on web design, Alice can help with back-end programming, and Charlie can assist as needed with C++.

4. Fitness Tracker App: Create a mobile app for tracking running workouts. Alice and Charlie can work on app development, while Bob designs the user interface.

5. E-commerce Website: Develop a website for a virtual store. Bob can lead the web design, while Alice and Charlie handle back-end programming.
    '''
    #testGenerator.Generate()
    testGenerator.ParseIdeas()

    # Create a VotingSystem with the test Generator
    votingSystem = VotingSystem(testGenerator)

    # Display the ideas
    votingSystem.DisplayIdeas()

    # Cast some votes
    votingSystem.CastVote(1, 2, 3)
    votingSystem.CastVote(1, 3, 2)
    votingSystem.CastVote(2, 1, 3)
    votingSystem.CastVote(3, 1, 2)
    votingSystem.CastVote(2, 3, 1)

    # Display the voting results
    votingSystem.DisplayResults()

    # Display the winning idea
    votingSystem.DisplayWinner()

    print("Succesful VotingService.py test!")
