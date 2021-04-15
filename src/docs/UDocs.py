from response.BadRespond import BadRespond
from helpers.RegexHelpers import uregex as re

from UMiddlewares import EnableCors

class UDocs:
    __docs_html = None
    __path = None
    __routes_paths = []

    def __init__(self, userver):
        self.__userver = userver

    def __validate_path(self, doc_path):
        if(re.match(r'[/][A-Za-z0-9/_-]*', doc_path) == False):
            raise Exception('[InvalidPath] The path for the documentation you set is incorrect. Check your path again.')
        if(len(doc_path) > 1 and doc_path[-1] == '/'):
            doc_path = doc_path[:-1]
        return doc_path

    def __get_html(self):
        try:
            with open('src/docs/index.html', 'r') as fil:
                data = "".join(fil.readlines())
            UDocs.__docs_html = data%('http://127.0.0.1:{}{}/json'.format(self.__userver.port, UDocs.__path))
        except:
            print('FileError: Can not open the path of documentation index.html.')

    @staticmethod
    def __expose_docs_html(req, res):
        if(UDocs.__docs_html != None):
            res.send_html(UDocs.__docs_html)
        else:
            BadRespond(res, req).send()

    @staticmethod
    def __expose_docs_json(req, res):
        response_json = {}
        for route in UDocs.__routes_paths:
            route_path = "".join(route[0])
            if(route_path != UDocs.__path and route_path != UDocs.__path + '/json'):
                response_json.update({ route_path: {
                    'method': route[2],
                    'description': route[3][0],
                    'status_codes': route[3][1]
                }})
        
        res.send_json(response_json)

    def start(self, path):
        UDocs.__routes_paths = self.__userver.router_paths
        UDocs.__path = self.__validate_path(path)
        self.__get_html()
    
        self.__userver.router.on(UDocs.__path, 'GET', UDocs.__expose_docs_html, [EnableCors], [])
        self.__userver.router.on(UDocs.__path + '/json', 'GET', UDocs.__expose_docs_json, [EnableCors], [])