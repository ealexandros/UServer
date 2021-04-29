from UServer import UServer

app = UServer(3000, host='0.0.0.0')

@app.router.get("/")
def index(req, res):
    # ..Business Logic..
    res.send_json({ "status": True})

@app.router.get("/person/json")
def index(req, res):
    # ..Business Logic..
    res.send_json({ "person": {}})

# ..You need to have a folder named static in your root path..
app.static('static/')

app.start(logger=True, block=True)