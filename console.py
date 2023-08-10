#!/usr/bin/python3
"""
Console for airnb clone console
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import re

class  HBNBCommand(cmd.Cmd):
    """
    class definition for the console
    """
    prompt = '(hbnb) '

    class_mapping = {
        'BaseModel': BaseModel,
        'User': User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
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

    def default(self, line):
       _class_mapping = {
           'all': self.do_all,
           'show': self.do_show
       }
       match = re.match(r"\w+\.\w+", line)
       if match:
           items = line.split('.')
           command = items[1].split('(')[0]
           if command in _class_mapping:
               param_s = re.search(r'\((.*?)\)', line).group(1)
               param_s = param_s.replace('"', '')
               param_s = param_s.replace("'", '')
               param = [arg.strip() for arg in param_s.split(',')]
               tmp_param = [items[0]] + param
               new_param = " ".join(x for x in tmp_param if x)
               return _class_mapping[command](new_param)
       print("*** Unknown syntax: {}".format(line))
       return False

    def do_create(self, cmmd):
        """Creates a class instance
        Usage: create <class>
        """
        if not cmmd:
            return self.error_helper("missing_class")
        args = cmmd.split(" ")
        if args[0] not in self.class_mapping:
            return self.error_helper('invalid_class')
        instance = (self.class_mapping)[args[0]]()
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
            if args[0] not in self.class_mapping:
                return self.error_helper('invalid_class')
            store = storage.all()
            key = "{}.{}".format(args[0], args[1])
            val = store.get(key)
            if val is None:
                return self.error_helper('no_instance')
            print(val)        
        else:
            return

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
            if args[0] not in self.class_mapping:
                return self.error_helper('invalid_class')
            store = storage.all()
            key = "{}.{}".format(args[0], args[1])
            val = store.get(key)
            if val is None:
                return self.error_helper('no_instance')
            del store[key]
            storage.save()
        else:
            return

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
                for k, v in store.items():
                    if k.split('.')[0] == args[0]:
                        obj_list.append(str(v))
        else:
            for item_obj in store.values():
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
        if args[0] not in self.class_mapping:
            return self.error_helper('invalid_class')
        if len(args) == 1:
            return self.error_helper('missing_id')
        if len(args) == 2:
            return self.error_helper('missing_attr')
        if len(args) == 3:
            return self.error_helper('missing_val')
        upd_key = "{}.{}".format(args[0], args[1])
        upd_obj = store.get(upd_key)
        if upd_obj is None:
            return self.error_helper('no_instance')
        banned = ["id", "created_at", "updated_at"]
        if args[2] not in banned:
            val = args[3].strip().strip('"').strip("'")
            setattr(upd_obj, args[2], val)
        storage.save()
        
    def do_EOF(self, line):
        """
        Handles end of file or quit
        """
        return True
    
    def do_quit(self, line):
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
