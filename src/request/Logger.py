from helpers.TerminalColors import tcolors

class Logger:
    def __init__(self):
        self.__active = None

    def action(self, __request):
        if(__request.method == None or __request.path == None or __request.http_version == None):
            print(tcolors.ERROR + '[CORRUPTED HEADER]'+ tcolors.ENDC + ' -> ' +
                    tcolors.BOLD + '{}:{}'.format(__request.addr, __request.port) + tcolors.ENDC)
        else:
            print(tcolors.method_color(__request.method) + '[' + __request.method + ']'+ tcolors.ENDC + ' ' +
                    tcolors.BOLD + __request.path + tcolors.ENDC + ' [FROM] ' + tcolors.BOLD + '{}:{}'.format(__request.addr, __request.port) + tcolors.ENDC)

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value if(type(value) == bool) else False