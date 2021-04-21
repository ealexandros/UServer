from UServer import UServer
from UMiddlewares import BodyJson

app = UServer(3000, host='0.0.0.0')

@app.router.restful('/user', middlewares=[BodyJson])
class user:
    def get(self, req, res):
        '''
            description: get 30 random users.

            status_codes: {
                "200": "OK",
                "400": "Not authorized"
            }
        '''
        # ..Business Logic.. #
        res.send_json({ "users": "..." })

    def post(self, req, res):
        '''
            description: create a person.
        '''
        # ..Business Logic.. #
        res.send_json({ "users": "..." })

    def delete(self, req, res):
        '''
            description: delete a person.

            status_codes: {
                "200": "OK",
                "400": "Not authorized"
            }
        '''
        # ..Business Logic.. #
        res.send_json({ "id": "..." })

app.start(block=True, logger=True)