#!/usr/bin/python3
"""
Console Module: designed for AirBnB.
using cmd module.
contains HBNBCommand class that represents the CLI.

Attributes:
    - prompt (str)
    - allclass (dict)
Methods:
    - emptyline()
    - do_quit()
    - do_EOF()
    - do_create()
    - do_show()
    - do_destroy()
    - do_all()
    - do_update()
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    CLI for AirBnB app

    Attributes:
        - prompt(str): command prompt display.
        - allclass (dict): dictionary for classnames and their objects.
    """

    prompt = "(hbnb) "

    allclass = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def emptyline(self):
        """Emptyline + ENTER doesnot execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctrl+D command to exit the program"""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of class, saves it and prints the id.
Usage: create <class name>"""

        args = line.split()
        if not args:
            print("** class name missing **")
            return

        classname = args[0]
        if classname not in self.allclass:
            print("** class doesn't exist **")
            return

        new = self.allclass[classname]()
        new.save()
        print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance,
based on the class name and id.
Usage: show <class name> <id>"""

        args = line.split()
        if not args:
            print("** class name missing **")
            return

        classname = args[0]
        if classname not in self.allclass:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = "{}.{}".format(classname, args[1])
        all_instances = storage.all()
        if instance_key not in all_instances:
            print("** no instance found **")
        else:
            instance = all_instances[instance_key]
            print(instance)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
Usage: destroy <class name> <id>"""

        args = line.split()
        if not args:
            print("** class name missing **")
            return

        classname = args[0]
        if classname not in self.allclass:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = "{}.{}".format(classname, args[1])
        all_instances = storage.all()
        if instance_key not in all_instances:
            print("** no instance found **")
            return

        del all_instances[instance_key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances,
based or not on the class name.
Usage: all
Usage: all <class name>"""

        args = line.split()
        all_instances = storage.all()
        if not args:
            instances_list = []
            for instance in all_instances.values():
                instances_list.append(str(instance))
            print(instances_list)

        else:
            classname = args[0]
            if classname not in self.allclass:
                print("** class doesn't exist **")
                return

            cls_instances = []
            for key, value in all_instances.items():
                if key.startswith(classname):
                    cls_instances.append(value)

            instances_list = []
            for element in cls_instances:
                instances_list.append(str(element))

            for instance in instances_list:
                print(instance)

    def do_update(self, line):
        """Updates an instance based on the class name and id,
by adding or updating attribute.
Usage: update <class name> <id> <attribute name> "<attribute value>" """

        args = line.split()
        if not args:
            print("** class name missing **")
            return

        classname = args[0]
        if classname not in self.allclass:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_key = "{}.{}".format(classname, args[1])
        all_instances = storage.all()
        if instance_key not in all_instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance = all_instances[instance_key]
        attr_name = args[2]
        attr_value = args[3]

        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                return

        setattr(instance, attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
