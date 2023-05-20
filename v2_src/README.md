**Note: This project is currently unfinished and represents the initial stages of a working database for the BrainstormBoost application. It serves as a starting point for further development and implementation.**

## Functionalities

The current functionalities available in the BrainstormBoost application are:

1. User Management
   - User registration: Users can create an account by providing a unique username, password, and name.
   - User login: Registered users can log in to their accounts using their credentials.
   - User deletion: Users can delete their accounts, which also deletes all associated data.

2. Group Management
   - Group creation: Users can create groups and become the group owners.
   - Group retrieval: Users can retrieve information about a specific group by its ID.
   - Group deletion: Group owners can delete their groups, which also deletes all associated data.

3. Member Management
   - Member addition: Group owners can add members to their groups.
   - Member removal: Group owners can remove members from their groups.

4. Idea Management
   - Idea creation: Group members can create new ideas within their groups.
   - Idea retrieval: Users can retrieve ideas associated with a specific group.
   - Voting: Group members can vote on ideas to express their preferences.

## Project Structure

The project follows the following directory structure:

- `db`: Contains scripts and files related to the database, including table creation and database connection.
- `models`: Contains Python classes that represent the data models used in the application.
- `repository`: Contains repository classes responsible for interacting with the database.
- `services`: Contains service classes that handle the business logic and provide functionality to the application.

Feel free to explore the directories and files to understand the implementation of each functionality.
