'''
    You can look the documentation of your applicaiton on, http://xxx.xxx.xxx.xxx:port/v1/docs.
    The Default path for the documentation is the `/docs`.
'''

from UServer import UServer
from UMiddlewares import EnableCors

app = UServer(port=3000, host='0.0.0.0')

@app.router.post('/person', middlewares=[EnableCors],
    description="You can create a new person by creating a json file with the `username`, `fnmae`, `password` and the `email`",
    return_codes={
        '200': 'person created',
        '404': 'json does not contain all the necessary fields',
        '409': 'person exist need to change email or password'
    })
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

@app.router.delete('/person/:id', docs=
    '''
        description: You can delete a person by providing only
        his id.

        return_codes: {
            "200": "person deleted",
            "400": "not authorized",
            "404": "person not found"
        }
    ''')
def delete_person(req, res):
    url_id = req.get_url('id')
    res.send_json({ 'id': url_id })

app.start(block=True, logger=True, doc_path='/v1/docs')