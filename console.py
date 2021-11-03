#!/usr/bin/python3
""" Console module entry point """


class HBNBCommand(cmd.Cmd):
    """ Class Holberton AirBnB clone """
    cmdloop():
        """ do the prompt """

    quit():
        """ Exit implementation """

    EOF():
        """ Not sure if this should be this way """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
