#!/usr/bin/python3
"""the entry point of the command interpreter"""
import cmd
import json
import os
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Define class HBHB Command"""

    prompt = "(hbnb) "
    list_class = ['BaseModel', 'User', 'Amenity', 'City',
                  'Place', 'Review', 'State']

    list_fnc = ['create', 'show', 'destroy', 'all', 'update', 'count']

    def precmd(self, arg):
        """Command imput"""
        if '.' in arg and '(' in arg and ')' in arg:
            my_cls = arg.split('.')
            my_fnc = my_cls[1].split('(')
            prm = my_fnc[1].split(')')
            if my_cls[0] in HBNBCommand.list_class and \
               my_fnc[0] in HBNBCommand.list_fnc:
                arg = my_fnc[0] + ' ' + my_cls[0] + ' ' + prm[0]

        return arg

    def do_quit(self, arg):
        """Method that quits command of program"""
        quit()

    def do_EOF(self, arg):
        """Method that quit program with CTRL-D"""
        print()
        quit()

    def emptyline(self):
        """Nothing to do with empty line"""
        pass

    def help_help(self):
        """Print help command description"""
        print("Provides description of a given command")

    def do_create(self, arg):
        """Create a new instance"""
        if len(arg) == 0:
            print("** class name missing **")

        elif arg not in HBNBCommand.list_class:
            print("** class doesn't exist **")

        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
