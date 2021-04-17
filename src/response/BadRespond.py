class BadRespond:
    '''
        This class sends an error response if a path is not defined in the UServer.__router_paths.

        :response:  This is a Response object.
        :request:   This is a Request  object.
    '''
    def __init__(self, response, request):
        self.responseObject = response
        self.responseObject.status = 500

        self.requestObject = request

        self.bad_request_html = '''
            <!DOCTYPE html>

            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Bad Request</title>
                </head>
                <body>
                    <p style="font-size: 0.9em">{} not supported on {} path.</p>
                </body>
            </html>
        '''.format(self.requestObject.method, self.requestObject.path)

    def send(self):
        accept_type = self.requestObject.header('Accept')
        if(accept_type == None):
            self.responseObject.send('{} not supported on {} path.'.format(self.requestObject.method, self.requestObject.path))
        elif('text/html' in accept_type or '*/*' in accept_type):
            self.responseObject.send_html(self.bad_request_html)