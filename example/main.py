from UServer import UServer

app = UServer(3000, host="0.0.0.0")

@app.get('/person/:id')
def cool(req, res):
    res.send_json({ 'response': req.url_param('id') })

app.start()

while(True):
    pass