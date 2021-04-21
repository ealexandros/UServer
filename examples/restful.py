from UServer import UServer
from UMiddlewares import BodyJson

app = UServer(3000, host='0.0.0.0')

@app.router.restful('/user', middlewares=[BodyJson], docs=
    '''
        description: this is a user based restful api.

        return_codes: {
            "200": "OK",
            "400": "Not authorized"
        }
    ''')
class user:
    def get(self, req, res):
        # ..Business Logic.. #
        res.send_json({ "users": "..." })

    def post(self, req, res):
        # ..Business Logic.. #
        res.send_json({ "users": "..." })

    def delete(self, req, res):
        # ..Business Logic.. #
        res.send_json({ "id": "..." })

app.start(block=True, logger=True)