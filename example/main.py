from UServer import UServer

app = UServer(3000, host="0.0.0.0")

@app.route
def cool(req, res):
    res.send_json({ 'response': True })

app.on('/status', cool)
app.on('/test', cool)

app.start()

while(True):
    pass