#!/usr/bin/python3
"""
HBNBCommand Module
===================
This module defines the command-line interpreter (CLI) for the Holberton BNB project.
It uses the `cmd` module to create an interactive shell for managing application objects.

Features:
- quit to exit the program
- More to be implementated

Classes:
    - HBNBCommand: Defines the command-line interface.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    ...
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
