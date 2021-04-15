from UServer import UServer

app = UServer(port=3000, host='0.0.0.0')

@app.router.get('/person/:id')
def get_person(req, res):
    url_id = req.url_param('id')
    # ..Business Logic.. #
    html = '''{}...'''.format(url_id)
    res.send_html(html)

@app.router.post('/person')
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

@app.router.delete('/person/:id')
def delete_person(req, res):
    url_id = req.url_param('id')
    # ..Business Logic.. #
    res.send_json({
        'id': url_id })

@app.router.put('/person/:id')
def change_person_info(req, res):
    url_id = req.url_param('id')
    fname = req.param('fname') # ../person/:id?fname=name
    # ..Business Logic.. #
    res.send_json({ 'person': {
        'id': url_id,
        'fname': fname }})

app.start(logger=True)

while(True):
    # ..More Business Logic.. #
    pass