from UServer import UServer

port = 3001
app = UServer(port=port, host='0.0.0.0')

@app.router.delete('/person/:id')
def delete_person(req, res):
    url_id = req.url_param('id')
    # ..Business Logic.. #
    res.send_json({
        'id': url_id
    })

@app.router.get('/person/:id', redirects=['/person/*/:id'])
def get_person(req, res):
    url_id = req.url_param('id')
    # ..Business Logic.. #
    res.send_json({
        'id': url_id
    })

@app.start(logger=True, function=True, block=True)
def start_func():
    print('starting on port: ' + port)

# ..This code will not be executed.. #