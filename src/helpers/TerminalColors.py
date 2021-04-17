class tcolors:
    '''
        This class helps with the logger class. It makes the
        console print look better.
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def method_color(method):
        if(method == 'POST' or method == 'PUT' or method == 'PATCH'):
            return tcolors.SUCCESS
        elif(method == 'GET' or method == 'OPTIONS'):
            return tcolors.OKCYAN
        elif(method == 'DELETE'):
            return tcolors.WARNING
        return tcolors.ENDC
        
