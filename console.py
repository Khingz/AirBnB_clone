#!/usr/bin/python3
"""
Console for airnb clone console
"""

import cmd

class  HBNBCommand(cmd.Cmd):
    """
    class definition for the console
    """
    prompt = '(hbnb) '

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
