#!/usr/bin/python3
"""
Console for airnb clone console
"""

import cmd
from models.base_model import BaseModel
from models import storage
import re

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
            "no_instance": "** no instance found **",
            "missing_attr": "** attribute name missing **",
            "missing_val": "** value missing **"
        }
        print(errors.get(error_type, "Error: Unknown error"))

    def do_create(self, cmmd):
        """Creates a class instance
        Usage: create <class>
        """
        if not cmmd:
            self.error_helper("missing_class")
        elif cmmd not in self.class_mapping:
            self.error_helper('invalid_class')
        else:
            instance = (self.class_mapping)[cmmd]()
            print(instance.id)
            instance.save()

    def do_show(self, cmmd):  
        """Print str rep of instance based on the class name and id
        Usage show <class> <id>
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
            store = storage.all()
            for item_dict in store.values():
                if item_dict['__class__'] == cls and item_dict['id'] == id:
                    item_obj = self.class_mapping[cls](**item_dict)
                    print(str(item_obj))
                    return
            return self.error_helper('no_instance')
        else:
            pass

    def do_destroy(self, cmmd):
        """Deletes instance based on the class name and id
        Usage: destroy <class> <id>
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
            store = storage.all()
            for item_key in list(store.keys()):
                k, _id = item_key.split(".")
                if k == cls and _id == id:
                    del store["{}.{}".format(cls, id)]
                    storage.save()
                    return
            return self.error_helper('no_instance')
        else:
            pass

    def do_all(self, cmmd):
        """Print all str rep of instance based or not on class name.
        Usage: all or all <class>
        """
        obj_list = []
        store = storage.all()
        if cmmd:
            args = cmmd.split(" ")
            if len(args) == 1:
                if args[0] not in self.class_mapping:
                    return self.error_helper('invalid_class')
                for item_dict in store.values():
                    if item_dict['__class__'] == args[0]:
                        cls = item_dict['__class__']
                        item_obj = self.class_mapping[cls](**item_dict)
                        obj_list.append(str(item_obj))
        else:
            for item_dict in store.values():
                cls = item_dict['__class__']
                item_obj = self.class_mapping[cls](**item_dict)
                obj_list.append(str(item_obj))
        print(obj_list)

    def do_update(self, cmmd):
        """Updates an instance based on the class name and id
        Usage: update <class> <id> <attr name> "<attr value>"
        """
        store = storage.all()
        if not cmmd:
            return self.error_helper("missing_class")
        args = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', cmmd)
        cls = args[0]
        if args[0] not in self.class_mapping:
            return self.error_helper('invalid_class')
        if len(args) == 1:
            return self.error_helper('missing_id')
        if len(args) == 2:
            return self.error_helper('missing_attr')
        if len(args) == 3:
            return self.error_helper('missing_val')
        for item_dict in store.values():
            if item_dict['__class__'] == cls and item_dict['id'] == args[1]:
                banned = ["id", "created_at", "updated_at"]
                if args[2] not in banned:
                    val = args[3].strip().strip('"').strip("'")
                    item_dict[args[2]] = val
                    storage.save()
                return
        return self.error_helper('no_instance')
        
            

    def do_EOF(self):
        """
        Handles end of file or quit
        """
        return True
    
    def do_quit(self):
        """Quits command to exit the program
        Usage: Quit
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
