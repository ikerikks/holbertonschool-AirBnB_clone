#!/usr/bin/python3
"""the entry point of the command interpreter"""
import cmd
import json
import os
import models
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

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_objs = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_objs.keys():
                print("** no instance found **")

            else:
                print(dict_all_objs[string])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif list_arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_objs = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_objs.keys():
                print("** no instance found **")

            else:
                del (dict_all_objs[string])
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        dict_all_objs = storage.all()
        list_objs = []

        if len(arg) == 0:
            for key, vals in dict_all_objs.items():
                list_objs.append(str(vals))
            print(list_objs)

        elif arg in HBNBCommand.list_class:
            for keys, vals in dict_all_objs.items():
                if vals.__class__.__name__ == arg:
                    list_objs.append(str(vals))
            print(list_objs)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")

        elif list_arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
            return

        elif len(list_arg) == 1:
            print("** instance id missing **")
            return

        else:
            dict_all_objs = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_objs.keys():
                print("** no instance found **")

            elif len(list_arg) == 2:
                print("** attribute name missing **")
                return

            elif len(list_arg) == 3:
                print("** value missing **")
                return

            else:
                setattr(dict_all_objs[string], list_arg[2], list_arg[3])
                storage.save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        count = 0
        list_arg = arg.split(" ")
        dict_all_objs = storage.all()
        for v in dict_all_objs.values():
            if v.__class__.__name__ == list_arg[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
