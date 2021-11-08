#!/usr/bin/python3
""" Console For AirBnb Clone """
import cmd
from models import BaseModel, User, Amenity, Review, City, Place, State
import inspect
import models

storage = models.storage


class HBNBCommand(cmd.Cmd):
    """ Class commands implementation """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exit the program on EOF detection """
        return True

    def do_quit(self, arg):
        """ Exit the program """
        return True

    def emptyline(self):
        """ do noting if blank line + enter is given """
        pass

    @staticmethod
    def check_for_braces(command, open_brace, close_brace):
        try:
            first_brace = command.index(open_brace)
            second_brace = command.index(close_brace)
            if command[second_brace + 1] == ")":
                return first_brace, second_brace
            else:
                return False, False
        except ValueError:
            return False, False

    def get_list_of_args(self, command):
        obj_id = ""
        attr = ""
        new_val = ""
        className = ""
        functionName = ""
        try:
            core_args = command.split("(")[0].split(".")  # User.update
            all_args = command.split("(")[1][:-1]  # *args + **kwargs
            className = core_args[0]
            functionName = core_args[1]
            if all_args != "":
                first_brace, second_brace = self.check_for_braces(all_args,
                                                                  "{", "}")
                if first_brace is not False:
                    arguments = all_args[:first_brace - 2]
                else:
                    arguments = all_args

                arguments = ' '.join(arguments.split())
                arguments = arguments.split(maxsplit=2, sep=",")
                obj_id = arguments[0].strip("\" ")
                attr = arguments[1].strip("\" ")
                try:
                    index_brace = arguments[2].index("]")  # if we found "["
                    new_val = arguments[2][:index_brace + 1].strip("\" ")
                except Exception:
                    new_val = arguments[2]
            return className, functionName, obj_id, attr, new_val
        except Exception as ex:
            return className, functionName, obj_id, attr, new_val

    def default(self, line):
        """ Implement overriten commands """
        first_brace, second_brace = self.check_for_braces(line, "{", "}")
        if first_brace is not False:
            core_string = line[:first_brace]
            str_dict = line[first_brace: second_brace + 1]
            dict_args = eval(str_dict)
            for key, val in dict_args.items():
                command = core_string + repr(key) + ', ' + repr(val) + ')'
                self.default(command)
            return
        try:
            args = self.get_list_of_args(line)

            if len(args) > 1:
                className, functionName, obj_id, attr, new_val = args
                if inspect.isclass(eval(className)) is True:
                    arg = className + ' ' + obj_id
                    if functionName == "all":
                        return self.do_all(className)
                    elif functionName == "show":
                        return self.do_show(arg)
                    elif functionName == "destroy":
                        return self.do_destroy(arg)
                    elif functionName == "update":
                        return self.do_update(arg + ' ' + attr + ' ' + new_val)
                    elif functionName == "count":
                        i = 0
                        object_container = storage.all()
                        for obj_id, obj in object_container.items():
                            if type(obj) is eval(className):
                                i += 1
                        print(i)
            else:
                print("*** Unknown syntax: {}".format(line))
                return False
        except Exception:
            pass

    def do_create(self, arg):
        """ Creation of new instance """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                args = arg.split()
                new_inst = eval("{}()".format(args[0]))
                new_inst.save()
                print(new_inst.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints instances """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                value = container_obj[key_id]
                print(value)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Destroy Instances """

        args = arg.split()
        container_obj = []
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                del container_obj[key_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Show the content of instance """
        storage.reload()
        container_obj = storage.all()
        args = arg.split()
        list_strings = []
        if len(args) == 0:
            for obj_id in container_obj.keys():
                obj = container_obj[obj_id]
                list_strings.append(str(obj))
            print(list_strings)
            return
        if len(args) == 1:
            try:
                eval(args[0])
                for obj_id in container_obj.keys():
                    if type(container_obj[obj_id]) is eval(args[0]):
                        obj = container_obj[obj_id]
                        list_strings.append(str(obj))
                print(list_strings)
            except Exception:
                print("** class doesn't exist **")
                return

    def do_update(self, arg):
        """ Change values inside instances """
        storage.reload()
        args = arg.split()
        length_args = len(args)
        if length_args == 0:
            print("** class name missing **")
            return
        if len(args) >= 1:
            try:
                eval(args[0])
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                try:
                    key_id = args[0] + "." + args[1]
                    container_obj = storage.all()
                    container_obj[key_id]
                except Exception:
                    print("** no instance found **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 2:
            try:
                eval(args[0])
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return

        if len(args) >= 3:
            try:
                eval(args[0])
                if len(args) == 3:
                    print("** value missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 4:
            args = " ".join(str(arg).split(maxsplit=3)).split(maxsplit=3)

            class_name = args[0]
            obj_id = args[1]
            obj_attr = args[2].strip("\"\'")
            obj_new_val = args[3]
            try:
                eval(class_name)
                key_id = class_name + "." + obj_id
                container_obj = storage.all()
                if key_id in container_obj:
                    obj = container_obj[key_id]
                    try:
                        type_attr = type(getattr(obj, obj_attr))
                        obj_new_val = self.same_type_as_attr(obj_new_val,
                                                             type_attr)
                        if obj_new_val is False:
                            return
                    except Exception:
                        obj_new_val = self.convert_new_val(obj_new_val)
                    setattr(obj, obj_attr, obj_new_val)
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            except Exception as ex:
                print("** class doesn't exist **")

    @staticmethod
    def same_type_as_attr(new_att, att_type):
        try:
            if att_type is list:
                try:
                    cast_list = eval("{}".format(str(new_att)))
                    for el in cast_list:
                        if type(el) is not str:
                            return False
                    return cast_list
                except SyntaxError:
                    return False
            if att_type is str:
                return att_type(new_att)
            value = att_type(new_att)
            if att_type is int or att_type is float:
                if new_att.isdigit():
                    value = int(new_att)
                elif new_att.replace(".", "").isdigit():
                    value = float(new_att)
                else:
                    return False
                if value < 0:
                    return False
            return value

        except ValueError:
            return False

    @staticmethod
    def convert_new_val(obj_new_val):
        """ Cast before setting it """
        try:
            if obj_new_val.isdigit():
                return int(obj_new_val)
            elif obj_new_val.replace(".", "").isdigit():
                return float(obj_new_val)
            elif type(eval(obj_new_val)) is list:
                return list(eval(obj_new_val))
            else:
                return obj_new_val
        except Exception:
            return obj_new_val

if __name__ == "__main__":
    HBNBCommand().cmdloop()
