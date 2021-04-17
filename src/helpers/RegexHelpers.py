try:
    import re
except:
    import ure

class uregex:
    '''
        This is an extention of the (re) library.
    '''
    @staticmethod
    def findall(regex, text):
        matches = []
        regex_result = re.search(regex, text)
        while(regex_result != None):
            matches.append(regex_result.group(0))
            text = text.replace(regex_result.group(0), "", 1)
            regex_result = re.search(regex, text)
        return matches

    @staticmethod
    def match(regex, text):
        regex_filter = re.compile(regex)
        return regex_filter.split(text) != None

    @staticmethod
    def split(regex, text):
        regex_filter = re.compile(regex)
        return regex_filter.split(text)

    @staticmethod
    def one_cut_split(regex, text):
        split_output = uregex.split(regex, text)
        return [split_output[0], "".join(split_output[1:])]