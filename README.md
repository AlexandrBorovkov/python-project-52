# Educational project "Task manager" #

### Tests and linter status:
[![Actions Status](https://github.com/AlexandrBorovkov/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AlexandrBorovkov/python-project-52/actions)
[![Build](https://github.com/AlexandrBorovkov/python-project-52/actions/workflows/build.yml/badge.svg)](https://github.com/AlexandrBorovkov/python-project-52/actions/workflows/build.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AlexandrBorovkov_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AlexandrBorovkov_python-project-52)

---

### Description: ###
Task Manager is a task management system. It allows you to set tasks, assign performers, and change their statuses. Registration and authentication are required to work with the system.

#### [Link to the deployed web application](https://python-project-52-zv20.onrender.com) ####

---

### The main objectives of the project: ###
#### Database Design ####
Creating data models using Django ORM.
Description of relationships between entities (One-to-Many, Many-to-Many).
#### Resource routing ####
Configuring URLs for typical CRUD operations.
Unification and simplification of work with operations of creation, reading, updating and deletion of data.
#### Forms and validation ####
Creating forms for entering and editing data.
Using Django's built-in mechanisms to generate forms and output errors.
#### Authorization and authentication ####
Implementation of user registration and login mechanisms.
Access rights management and control of user actions.
#### Data filtering ####
Creates forms for filtering tasks.
Using libraries to simplify the filtering process.
#### Monitoring and error notifications ####
Integration of the Roll bar service for error collection and notification.
Setting up notifications in Slack, via email, and other channels.

---

### How do I launch the app? ###
1. **Clone the repository**:
   ```sh
   git clone https://github.com/AlexandrBorovkov/python-project-52.git
   ```
   or
   ```sh
   git clone git@github.com:AlexandrBorovkov/python-project-52.git
   ```
2. **Set up environment variables (`.env`)**:
   ```sh
   DATABASE_URL=postgresql://user:password@localhost:5432/database
   SECRET_KEY=your_secret_key
   ROLLBAR_TOKEN=your_token
   ```
3. **Installing dependencies and creating database tables**:
   ```sh
   make build
   make install
   make migrate
   ```
4. **Run the application**:
   - In **development**:
    ```sh
    make start
    ```
   - In **production**:
    ```sh
    make render-start
    ```
