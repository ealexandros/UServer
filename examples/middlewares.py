from UServer import UServer
from UMiddlewares import BodyParser, ParamValidation

app = UServer(port=3000, host='0.0.0.0')

def intercept(req, res):
    print('I am a middleware..')
    if(req.port == 1000):
        return True
    return Exception('wrong port number')

@app.router.post('/person', middlewares=[BodyParser, ParamValidation, intercept])
def create_person(req, res):
    fname = req.body('fname')
    lname = req.body('lname')
    username = req.body('username')
    password = req.body('password')
    # ..Business Logic.. #
    res.send_json({ 
        'fname': fname,
        'lname': lname,
        'username': username,
        'password': password })

app.start(block=True)