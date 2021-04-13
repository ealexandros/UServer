from UServer import UServer
from UMiddlewares import BodyJson

app = UServer(3000, host="0.0.0.0")

@app.router.get('/person/:id', middlewares=[BodyJson])
def cool(req, res):
    res.send_json({ 'response': req.url_param('id') })

app.static('./src')

app.start()

while(True):
    pass