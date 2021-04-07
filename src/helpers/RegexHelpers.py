try:
    import re
except:
    import ure

class uregex:
    @staticmethod
    def findall(regex, text):
        matches = []
        regex_result = re.search(regex, text)
        while(regex_result != None):
            matches.append(regex_result.group(0))
            text = text.replace(regex_result.group(0), "\b", 1)
            regex_result = re.search(regex, text)
        return matches