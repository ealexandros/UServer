# Documentation ![version](https://img.shields.io/badge/version-1.0.0-brightengreen)

In **README.md** file you wil find the complete documentation of the `UServer` repository. This file may be chnaged over the time, because more functionality will be added to the project.

So lets start!

## 📚 Table of Content

- [Boot](#-boot,py)
    - [ENV](#env-module)
    - [ENV tutorial](#how-env-works)
- [Setup](#-setup.py)
    - [Basic Setup](#basic-setup)
    - [Routes](#routes)
    - [URL Params](#url-params)
    - [App Start](#app-start)
- [Middlewares](#-middlewares)
- [Options](#-options)

## ▶ Boot.py

In the [boot.py](https://github.com/alexandros44/UServer/blob/main/examples/boot.py) file the only thing required is to connect to your AP device (router etc). You can find more about that in the link [here](https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html).

### ENV Module
The only new thing in the **boot.py** file is the `env` module. The `env` module cames with the UServer package. It stores variables in a seperate file for a more secure code. You do not want to have your **SSID** or your **PASSWORD** inside your code. 

### How ENV works
In order to use it you need to have a `.env` file created, like in the [.env.example](https://github.com/alexandros44/UServer/blob/main/examples/.env.example). After making the file you need to load it with the next two commnads,

```python
from env import dotenv 

env = dotenv(*path*)
env.scan()

print(env[*variable_name*])
```

In the code above you can find two variables inside a \*_\*. Those variables must be:

1. **path**, the relative path to the .env
2. **variable_name**, the name of the variable you want. If that variable does not exist you will get a None. For example in the [.env.example](https://github.com/alexandros44/UServer/blob/main/examples/.env.example) we could use the `env['SSID']`.

## 💻 Setup.py

In order to understand how this library works we need to start from the [setup.py](https://github.com/alexandros44/UServer/blob/main/examples/setup.py) file. So lets start to find out how all works.

### Basic Setup
In the first step you need to create a UServer `app`. In the setup.py file we can see it in the **3** line.
```python
app = UServer(port=*port*, host='127.0.0.1')
```

Where the \*port\* is the port we would like host the application in. The `host` field by default will be `127.0.0.1` the loopback address or localhost. You can change it to whatever you like. For example `0.0.0.0`.

### Routes

Create different routes. More specifically you can use the,
```python
@app.router.get(*path*)
@app.router.post(*path*)
@app.router.delete(*path*)
@app.router.put(*path*)
@app.router.patch(*path*)
@app.router.options(*path*)
```

### Functions

As we see all the functions inside the decorator have two parameters. The first parameter is the request, which contains everything that has to do with the HTTP request and the second parameter has to do with the response of the request.

For example,
```python
@app.router.put('person/:id')
def change_person_info(req, res):
    url_id = req.url_param('id')
    res.send('this is your id' + url_id)
```

### URL params

For creating **get, post, delete, put, etc** routes. The path in the \*path\* should be the path you would like to create. You also can create different type of url parameters. For example in the setup.py we can see on the line 5 we have a `/:id`. The :id is a parameters which we can get with the next command,
```python
param = req.url_param('id')
```

You will get a None if the parameter you are looking for does not exist.

### App Start

In order to start the server you need to execute the next command,
```python
app.start()
```
Or you can execute a function before starting the server with the following method,

For Example,
```python
@app.start(function=True)
def starting():
    print('The server is starting after this function')
    print('Server running on port' + port)

```

```
Output: The server is starting after this function
        Server running on port *port_number*
```

The `app.start()` command can take the following parameters,

1. logger=(True, default=Flase), which will log every HTTP request that comes to you.
2. block=(True, default=Flase), if the blocking is True then the code below your start command will not run.
3. function=(True default=False), executes a predifined function before starting the server.