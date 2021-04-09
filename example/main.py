from UServer import UServer

app = UServer(3000, host="0.0.0.0")

def cooler(req, res):
    print(100)
    return True

@app.get('/person/:id', middlewares=[cooler])
def cool(req, res):
    res.send_json({ 'response': req.url_param('id') })

app.start()

while(True):
    pass