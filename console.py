#!/usr/bin/python3
"""
Console for airnb clone console
"""

import cmd
from models.base_model import BaseModel

class  HBNBCommand(cmd.Cmd):
    """
    class definition for the console
    """
    prompt = '(hbnb) '

    class_mapping = {
        'BaseModel': BaseModel
    }

    def error_helper(self, error_type):
        """Helper function to print error messages using a dictionary"""
        errors = {
            "missing_class": "** class name missing **",
            "invalid_class": "** class doesn't exist **",
        }
        print(errors.get(error_type, "Error: Unknown error"))

    def do_create(self, cls):
        """creates a class instance"""
        if not cls:
            self.error_helper("missing_class")
        elif cls not in self.class_mapping:
            self.error_helper('invalid_class')
        else:
            instance = (self.class_mapping)[cls]()
            instance.save()
            print(instance.id)


    def do_EOF(self, line):
        """
        Handles end of file or quit
        """
        return True
    
    def do_quit(self, args):
        """Quits command to exit the program"""
        return True
    
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    try:       
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
