import sys

try:
    import os
except:
    import uos as os

class upath:
    @staticmethod
    def get_correct_slash():
        if(sys.platform[0:3] == 'win'):
            return '\\'
        return '/'

    @staticmethod
    def isfile(fname):
        try:
            fil = open(fname, "r")
            fil.close()
            return True
        except OSError:
            return False

    @staticmethod
    def walk(root):
        files = []
        dirs = []

        for dirent in os.listdir(root):
            if(upath.isfile(root + upath.get_correct_slash() + dirent)):
                files.append(dirent)
            else:
                dirs.append(dirent)
        yield root, dirs, files

        for i in dirs:
            yield from upath.walk(root + upath.get_correct_slash() + i)