import cmd
import readline
import rlcompleter
from models.base_model import BaseModel
from models import storage
import json

# enable tab completion
readline.parse_and_bind("tab: complete")

# command history setup
HISTORY_FILE = ".cmd_history"

try:
    # load commnad history if it exists
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass  # if no history file is found


# function to inform user when error encountered
def inform_user_given_one_arg(arg):
    if arg == "":
        print("** class name missing **")
    elif arg != "BaseModel":
        print("** class doesn't exist **")
    else:
        print("** instance id missing **")

def inform_user_given_two_arg(class_name):
    if class_name != "BaseModel":
        print("** class doesn't exist **")
    else:
        print("** no instance found **")

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_salute(self, arg):
        print("Hey, Aimable")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Have a Good Day!")
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        self.do_quit(self)

    def emptyline(self):
        """if not command given re-prompt"""
        return False

    def do_create(self, arg):
        if arg.strip() == "BaseModel":
            instance = BaseModel()
            instance.save()
            print(instance.id)
        elif arg.strip() != "BaseModel":
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):

        try:
            class_name, id = arg.split()
            all_objs = storage.all()
            key = ".".join([class_name, id])
            if key in all_objs.keys():
                all_objs = storage.all()
                print(all_objs[key])
            else:
                inform_user_given_two_arg(class_name)
        except ValueError:
            inform_user_given_one_arg(arg)

    def do_destroy(self, arg):
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

    def do_all(self, arg="BaseModel"):
        all_objs = storage.all()
        all = []
        for key in all_objs.keys():
            all.append(str(all_objs[key]))
        print(all)

    def do_update(self, arg): ...


if __name__ == "__main__":
    try:
        HBNBCommand().cmdloop(intro="Welcome to Holberton BNB")
    finally:
        readline.write_history_file(HISTORY_FILE)
