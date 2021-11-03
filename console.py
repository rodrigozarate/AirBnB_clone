#!/usr/bin/python3
""" Console module entry point """


class HBNBCommand(cmd.Cmd):
    """ Class Holberton AirBnB clone """
    prompt = '(hbnb) '

    def cmdloop():
        """ do the prompt """

    def quit():
        """ Exit implementation """
        return True

    def EOF():
        """ Not sure if this should be this way """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
