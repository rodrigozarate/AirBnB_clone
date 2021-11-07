#!/usr/bin/python3
""" Console HBNB Clone """
import cmd
from models import *


class HBNBCommand(cmd.Cmd):
    """ Clas to define basic commands of console """
    prompt = '(hbnb) '

    def quit(self, arg):
        """ do quit """
        return True

    def EOF(self, arg):
        """ Detect End Of File """
        return True

    def emptyline(self):
        """ do nothing """
        pass

    def check_for_class(self, args):
        """ Evaluate arguments and existance """
        if len(args) == 0:
            print("** class name missing **")
            return False
        else:
            try:
                check = eval("{}()".format(args[0]))
                dict = storage.all()
                del dict[args[0] + "." + check.id]
                return True
            except:
                print("** class doesn't exist **")
                return False

    def check_for_id(self, args):
        """ Evaluate arguments and instance id """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        key = args[0] + "." + args[1]
        if key in storage.all():
            return True
        else:
            print("** no instance found **")
            return False

    def check_for_attribute(self, args):
        """ Check existance of attributes """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        elif len(args) < 4:
            print("** value missing **")
            return False
        elif args[3] in ['id', 'created_at', 'created_at']:
            return False
        else:
            return True

    def create(self, args):
        """ Create new instance """
        className = args.split()
        if self.check_for_class(className):
            new_instance = eval("{}()".format(className[0]))
            new_instance.save()
            print(new_instance.id)

    def show(self, arg):
        """ Show arguments of instance """
        class_id = arg.split()
        if self.check_for_class(class_id) and self.check_for_id(class_id):
            dict = storage.all()
            print("{}".format(dict[class_id[0] + "." + class_id[1]]))

    def destroy(self, args):
        """ Destroy the instance """
        class_id = args.split()
        if self.check_for_class(class_id) and self.check_for_id(class_id):
            dict = storage.all()
            del dict[class_id[0] + "." + class_id[1]]
            storage.save()

    def all(self, args):
        """ Print all clases of instance """
        newlist = []
        args_sp = args.split()
        for key, value in storage.all().items():
            className = key.split(".")
            if len(args) == 0:
                newlist.append(value.__str__())
            elif className[0] == args_sp[0]:
                newlist.append(value.__str__())
        if bool(newlist) is False:
            print("** class doesn't exist **")
        else:
            print(newlist)

    def update(self, args):
        """ Update current instance """
        args_sp = args.split()
        if (self.check_for_class(args_sp) and self.check_for_id(args_sp) and
                self.check_for_attribute(args_sp)):
            args_sp[3] = args_sp[3].strip('"')
            class_id = args_sp[0] + "." + args_sp[1]
            attribute = args_sp[2]
            upd_instance = storage.all().get(class_id)
            try:
                upd_attr = getattr(upd_instance, attribute)
            except:
                upd_attr = ""
            type_attr = type(upd_attr)
            setattr(upd_instance, attribute, type_attr(args_sp[3]))
            upd_instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
