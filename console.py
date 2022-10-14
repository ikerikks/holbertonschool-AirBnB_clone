#!/usr/bin/python3
"""import module"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command line"""

    prompt = "(hbnb)"

    def do_quit(self, args):
        """quit"""
        return True

    def do_EOF(self, args):
        """end"""
        return True

    def help_quit(self):
        """help"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """empty"""
        pass

    def do_create(self, args):
        """
        creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        token_str = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_inst = eval(token_str[0])()
            new_inst.save()
            print(new_inst.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        prints the string representation of an instance based on the class name
        """
        token_str = args.split()
        if len(token_str) == 0:
            print("** class name missing **")
            return
        try:
            eval(token_str[0])
        except Exception:
            print("** class doesn't exist **")
        if len(token_str) == 1:
            print("** instance id missing **")
            return
        obj_dictionary = storage.all()
        try:
            value = (obj_dictionary[token_str[0] + "." + token_str[1]])
            print(value)
        except Exception:
            print("** no instance found **")

    def do_destroy(self, args):
        """deletes an instance based on the class name and id"""
        token_str = args.split()

        if len(token_str) == 0:
            print("** class name missing **")
            return
        try:
            eval(token_str[0])
        except Exception:
            print("** class doesn't exist **")
        if len(token_str) == 1:
            print("** instance id missing **")
        else:
            obj_dictionary = storage.all()
            string = f.{token_str[0]}.{token_str[1]}
            if string not in obj_dictionary.keys():
                print("** no instance found **")
            else:
                del (obj_dictionary[string])
                storage.save()

    def do_all(self, args):
        """
        prints all string representation of all instances
        based or not on the class name
        """
        token_str = args.split()
        try:
            eval(token_str[0])
        except Exception:
            print("** class doesn't exist **")
        objects = storage.all()
        new_list = []
        for key, value in objects.items():
            object_name = value.__class__.__name__
            if object_name == token_str[0]:
                new_list = new_list + [value.__str__()]
                print(new_list)

    def do_update(self, args):
        """
        updates an instance based on the class name
        and id by adding or updating attribute
        """
        token_str = args.split()
        if len(token_str) == 0:
            print("** class name missing **")
            return
        try:
            eval(token_str[0])
        except Exception:
            print("** class doesn't exist **")
        if len(token_str) == 1:
            print("** instance id missing **")
            objects = storage.all()
            for key, value in objects.items():
                object_name = value.__class__.__name__
                object_id = val_id
                if object_name == (token_str[0] and
                                   object_id == token_str[1].strip('"')):
                    if len(token_str) == 2:
                        print("** attribute name missing **")
                    elif len(token_str) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, token_str[2], token_str[3])
                        storage.save()
                        return
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
