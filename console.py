#!/usr/bin/python3
"""
Console for airnb clone console
"""

import cmd
from models.base_model import BaseModel
from models import storage

class  HBNBCommand(cmd.Cmd):
    """
    class definition for the console
    """
    prompt = '(hbnb) '

    class_mapping = {
        'BaseModel': BaseModel
    }

    def error_helper(self, error_type):
        """Helper function to print error msg using a dict"""
        errors = {
            "missing_class": "** class name missing **",
            "invalid_class": "** class doesn't exist **",
            "missing_id": "** instance id missing **",
            "no_instance": "** no instance found **"
        }
        print(errors.get(error_type, "Error: Unknown error"))

    def do_create(self, cmmd):
        """
        creates a class instance
        """
        if not cmmd:
            self.error_helper("missing_class")
        elif cmmd not in self.class_mapping:
            self.error_helper('invalid_class')
        else:
            instance = (self.class_mapping)[cmmd]()
            instance.save()
            print(instance.id)

    def do_show(self, cmmd):
        """
        Prints the string representation of an instance 
        based on the class name and id
        """
        if not cmmd:
            return self.error_helper("missing_class")
        args = cmmd.split(" ")
        if len(args) == 1:
            return self.error_helper('missing_id')
        if len(args) == 2:
            cls = args[0]
            id = args[1]
            if cls not in self.class_mapping:
                return self.error_helper('invalid_class')
            store = storage.__dict__
            for item in store.values():
                for inst in item:
                    data = item[inst]
                    if data['__class__'] == cls and data['id'] == id:
                        return print(self.class_mapping[cls](data))
                    return self.error_helper('no_instance')
        else:
            pass


    def do_EOF(self, line):
        """
        Handles end of file or quit
        """
        return True
    
    def do_quit(self, args):
        """
        Quits command to exit the program
        """
        return True
    
    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    try:       
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        pass
