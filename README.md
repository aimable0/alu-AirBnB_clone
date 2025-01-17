# HBNBCommand - Holberton BNB Command Line Interpreter

## Project Description

The **Holberton BNB (HBNB)** project is designed to provide an interactive shell
for managing various objects related to the Holberton BNB application. This
command-line interface (CLI) allows users to create, display, update, and delete
objects from storage, among other features. The objects include models such as
BaseModel, User, State, City, Amenity, Place, and Review.

## Command Interpreter Description

The command-line interpreter allows users to interact with instances of various
classes (such as BaseModel, User, State, etc.) and perform actions like:
Creating new instances
Displaying instances
Deleting instances
Updating instance attributes

### Features
Object creation, display, deletion, and updates.
Interaction with models such as BaseModel, User, State, City, Amenity, Place, and Review.
Command history using the readline module.

## How to Start the Interpreter
To start the interpreter, run the following command in your terminal:
bash
./console.py or python3 console.py

This will launch the interactive shell. You should see the prompt:

  >  (hbnb)

##How to Use the Command Interpreter

Once the interpreter is running, you can use the following commands to interact with it:

1. **Create a New Instance**:
    - Syntax: `create <class name>`
    - Example:
           create User
           This will create a new instance of the `User` class and print the instance ID.

2. **Display an Instance**:
    - Syntax: `show <class name> <id>`
    - Example:
           show User 12345
           This will display the instance of `User` with the ID `12345`.

3. **Delete an Instance**:
    - Syntax: `destroy <class name> <id>`
    - Example:
           destroy User 12345
           This will delete the instance of `User` with the ID `12345`.

4. **Display All Instances**:
    - Syntax: `all <class name>`
    - Example:
           all User
           This will display all `User` instances. If no class name is provided, it will display all instances.

5. **Update an Instance**:
    - Syntax: `update <class name> <id> <attribute name> <attribute value>`
    - Example:
           update User 12345 name "John Doe"
      ```
      This will update the name attribute of the User instance with the ID 12345 to "John Doe".
