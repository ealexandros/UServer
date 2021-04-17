try:
    import json
except:
    import ujson as json

class BodyParser:
    '''
        Parses the body of the HTTP (HyperText Transfer Protocol) request.

        :body:  The request body in a String format.
    '''
    def __init__(self, body):
        self.__raw_body = body

    def _get_parse_object(self, content_type):
        try:
            if(content_type == 'application/json'):
                return self.__parse_json()
            elif(content_type == 'application/x-www-form-urlencoded' or content_type == 'params'):
                return self.__parse_form()
        except:
            print('ValueError: Can not read the body or params from the request.\nFile: BodyParser.py')

        return {
            '__raw__': self.__raw_body
        }

    def __parse_form(self):
        raw_body_split = list(map(lambda params: params.split('='), self.__raw_body.split('&')))

        body_json = {}
        for key, value in raw_body_split:
            body_json[key] = value
        return body_json

    def __parse_json(self):
        return json.loads(self.__raw_body)
