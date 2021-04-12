import os

class dotenv:
    def __init__(self, rpath):
        self.__rpath = rpath
        self.__variables = {}

    def scan(self):
        with open(self.__rpath, 'r') as fil:
            variables = fil.readlines()

        for var in variables:
            var_no_comment = var.split('#')[0].strip()
            if(var_no_comment.count('=') == 1):
                key, value = var_no_comment.split('=')
                if(key.strip() != '' and ' ' not in key):
                    self.__variables.update({ key: value })

    def __getitem__(self, arg):
        if(arg in self.__variables):
            return self.__variables[arg]
        return None

    