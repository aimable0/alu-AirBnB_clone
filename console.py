#!/usr/bin/python3
"""
HBNBCommand Module
===================
Module: command-line interpreter (CLI) for the Holberton BNB project.
It uses the `cmd` module to:
    -create an interactive shell for managing application objects.

Features:
# - Tab completion for commands.
# - Command history using the readline module.
- Object creation, display, deletion, and more.

Classes:
    - HBNBCommand: Defines the command-line interface.
"""

import cmd
import readline
import rlcompleter
from models.base_model import BaseModel
from models import storage
import json

# Enable tab completion
readline.parse_and_bind("tab: complete")

# Command history setup
HISTORY_FILE = ".cmd_history"

try:
    # Load command history if it exists
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass  # No history file found, proceed silently


def inform_user_given_one_arg(arg):
    """
    Inform the user about missing or invalid arguments.

    Args:
        arg (str): The argument provided by the user.

    Prints:
        - "** class name missing **" if no argument is provided.
        - "** class doesn't exist **" if the class name is invalid.
        - "** instance id missing **" for incomplete commands.
    """
    if arg == "":
        print("** class name missing **")
    elif arg != "BaseModel":
        print("** class doesn't exist **")
    else:
        print("** instance id missing **")


def inform_user_given_two_arg(class_name):
    """
    Inform the user about invalid or missing instances.

    Args:
        class_name (str): The class name provided by the user.

    Prints:
        - "** class doesn't exist **" if the class name is invalid.
        - "** no instance found **" if the instance doesn't exist.
    """
    if class_name != "BaseModel":
        print("** class doesn't exist **")
    else:
        print("** no instance found **")


class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for managing Holberton BNB objects.

    Attributes:
        prompt (str): The command prompt displayed to the user.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exits the program.

        Args:
            arg (str): Optional argument (not used).

        Usage:
            quit
        """
        print("Have a Good Day!")
        return True

    def do_EOF(self, arg):
        """
        Exits the program when EOF is encountered.

        Args:
            arg (str): Optional argument (not used).

        Usage:
            EOF (press Ctrl+D)
        """
        return True

    def emptyline(self):
        """
        Prevents the shell from repeating the last command on an empty line.

        Returns:
            False: Ensures the prompt is displayed again.
        """
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel and saves it to storage.

        Args:
            arg (str): The class name ("BaseModel").

        Usage:
            create BaseModel
        """
        if arg.strip() == "BaseModel":
            instance = BaseModel()
            instance.save()
            print(instance.id)
        else:
            if arg == "":
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Displays the string representation of an object.

        Args:
            arg (str): The class name and ID separated by a space.

        Usage:
            show BaseModel <id>
        """
        try:
            class_name, id = arg.split()
            all_objs = storage.all()
            key = ".".join([class_name, id])
            if key in all_objs.keys():
                print(all_objs[key])
            else:
                inform_user_given_two_arg(class_name)
        except ValueError:
            inform_user_given_one_arg(arg)

    def do_destroy(self, arg):
        """
        Deletes an object from storage.

        Args:
            arg (str): The class name and ID separated by a space.

        Usage:
            destroy BaseModel <id>
        """
        try:
            class_name, id = arg.split()
            all_objs = storage.all()
            key = ".".join([class_name, id])
            if key in all_objs.keys():
                storage.delete(key)
            else:
                inform_user_given_two_arg(class_name)
        except ValueError:
            inform_user_given_one_arg(arg)

    def do_all(self, arg):
        """
        Displays all objects in storage or all objects of a specific class.

        Args:
            arg (str): The class name (optional).

        Usage:
            all [BaseModel]
        """
        if arg == "" or arg == "BaseModel":
            all_objs = storage.all()
            all_list = []
            for key in all_objs.keys():
                all_list.append(str(all_objs[key]))
            print(all_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an object's attributes.

        Args:
            arg (str): The class name, ID, attribute name, and value.

        Usage:
            update <class name> <id> <attribute name> <attribute value>
        """
        try:
            class_name, id, attr_name, attr_value = arg.split()
            all_objs = storage.all()
            key = ".".join([class_name, id])
            if class_name == "BaseModel" and key in all_objs.keys():
                instance = all_objs[key]
                setattr(instance, attr_name, attr_value)
                instance.save()
            elif class_name == "BaseModel":
                print("** no instance found **")
            else:
                print("** class doesn't exist **")
        except ValueError:
            # when some values are missing
            if arg == "":
                print("** class name missing **")
            elif len(arg.split()) == 1 and arg.split()[0] == "BaseModel":
                print("** instance id missing **")
            elif arg.split()[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(arg.split()) == 2:
                print("** attribute name missing **")
            elif len(arg.split()) == 3:
                print("** value missing **")


if __name__ == "__main__":
    """
    Entry point for the command-line interpreter.
    Initializes and starts the command loop.
    """
    HBNBCommand().cmdloop()
    readline.write_history_file(HISTORY_FILE)
