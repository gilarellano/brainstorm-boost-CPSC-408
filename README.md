# Project Description
#### By: Gilberto Arellano, Luis Rivas, Darron Kotoyan
BrainstormBoost is a novel software program aimed at facilitating effective group idea generation. Leveraging the impressive AI capabilities of OpenAI's GPT model, the application allows users to send detailed information about their group, including each member's skills, interests, and the group's project proposal. The AI then produces five potential ideas, which the group members can vote on to decide on a course of action that best suits everyone.

# Project Structure and Progress
Our project is divided into two main directories, `v1_src/` and `v2_src/`, representing the two main iterations of our work.

## `v1_src/`
The `v1_src/` directory contains the first iteration of BrainstormBoost, featuring a front-end application built using JavaScript and Flask. Despite not having a functioning database at this point, this version laid down the groundwork for the project, enabling us to better understand the architecture and feature requirements of the application. This directory mainly consists of the client and server, the client for the frontend and the server for backend business logic.

## `v2_src/`
Realizing the importance of a solid back-end for the smooth operation of the application, we made a strategic pivot towards developing a working database in the `v2_src/` version. In this iteration, the back-end of the software has been structured into four distinct directories for better management:

- `db/`: This directory contains all the necessary files related to the database, including its creation and queries.
- `models/`: This holds the Object-Oriented Programming (OOP) class structure for the project.
- `repository/`: This directory contains the logic to manage services and models and effectively connect them to the database.
- `services/`: This holds the business logic of our models.

With this version, we have managed to establish a robust back-end structure. We have seamlessly integrated our models, repositories and services, and have successfully connected them to our database.

## Future Directions
The next phase of our project will involve integrating the back-end with the front-end. With the database and business logic in place, we're now well equipped to develop a front-end that provides an intuitive and seamless user experience.

We also plan to improve the AI idea generation feature, making the outputs more tailored and relevant to the specific inputs provided by the user.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
