# Documentation ![version](https://img.shields.io/badge/version-1.0.2-brightengreen)

In **README.md** file you wil find the complete documentation of the `UServer` repository. This file may be chnaged over the time, because more functionality will be added to the project.

So lets start!

## 📚 Table of Content

- [Boot](#-boot,py)
    - [ENV](#env-module)
    - [ENV tutorial](#how-env-works)
- [Setup](#-setup.py)
    - [Basic Setup](#basic-setup)
    - [Routes](#routes)
    - [Functions](#functions)
        - [Request](#request)
        - [Response](#response)
    - [Paths and Redirects](#paths-and-redirects)
    - [URL Params](#url-params)
    - [App Start](#app-start)
- [Middlewares](#-middlewares)
    - [UMiddlewares.py](#umiddlewares.py)
    - [Middleware Setup](#middleware-setup)
    - [Error Overriding](#error-overriding)
    - [Middleware Queue](#middleware-queue)
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

##### Request

The request class has the next properties,

```
1. req.method       ->  gives the method `POST, DELETE etc`.
2. req.path         ->  gives the path `/person/18467124`.
3. req.path_list    ->  gives the path as a list `['/person', '18467124']`.
4. reg.http_version ->  gives the HTTP version `1.1, 2 etc`.
5. req.addr         ->  gives the IP address of the client `192.168.1.10`.
6. req.port         ->  gives the port of the client `12847`.
7. req.content_type ->  gives the content type of the body `text/html`.
```

The __request class has the next methods,

```
1. req.url_param(\*param_name\*)    ->  gets the url params `:id`.
2. req.body(\*param_name\*)         ->  gets the application body. If the body is not a json file, for the *param_name* type `__raw__` and you will get the hole body.

3. req.param(\*param_name\*)        ->  gets the params of the request `?test=true`.
4. req.header(\*header_name\*)      ->  gets a header `Content-Type etc`.
```

All of the above functions will return None if they wont find the parameter you are looking.

##### Response

The response class has the next properties,

```
1. status   ->  gives the status code that we will send back.
```

The response class has the next methods,

```
1. res.send_plain(*data*, *extra_headers*)      ->  sends plain text.
2. res.send_json(*data*, *extra_headers*)       ->  sends json.
3. res.send_html(*data*, *extra_headers*)       ->  sends html.
4. res.send_css(*data*, *extra_headers*)        ->  sends css.
5. res.send_javascript(*data*, *extra_headers*) ->  sends jsvascript.
6. res.send_xml(*data*, *extra_headers*)        ->  sends xml.
7. res.cors(*cors_flag*)                        ->  adds cors header flag.
```

All of the above methods can take extra headers. the headers **must** be an object. For example,

```python
headers = {
    'Content-Type': 'text/css',
    'Server': 'ESP'
}
```

### Paths and Redirects

For the path you need to construct it like below,
```
/person/:id
/test/*
/test/*/:id
```

In the path we can add url_params `/:id`, which are explained [here](#url-params). There are also the `*` which matches every path possible. For example, if we take the `/test/*/:id` in the code above in order to match that path we will need to go to `/test/*random*/*id*`.

If you would like to redirect a client to your desired path you can do it like this,
```python
@app.router.*request_method*(*path*, redirects=['/*', '/*/test'])
```

You can have as many redirects as you want, although they must be valid. If not an `Exception` will be executed.

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

1. **logger**, which will log every HTTP request that comes to you.
2. **block**, if the blocking is True then the code below your start command will not run.
3. **function**, executes a predifined function before starting the server.
4. **show_doc**, enables the auto documentation.
5. **doc_path**, which will change the default path for the documentation.

The first 1-4 parameters can take ```True or False```. Their default value of is False, except for the 4 which is True. Lastly, the 5 parameters can take a valid string path. Its default value is /docs.

## 🔀 Middlewares.py

For better understanding of the middlewares in the userver package you can see the [middlewares.py](https://github.com/alexandros44/UServer/blob/main/examples/setup.py) file. Lets start to analyze that file.

**P.S**: Some parts of the file will be skipped because we have already talked about them. However, every part that we skip there will be a reference in the documentation.

### UMiddlewares.py

First of all we import the UMiddlewares library that cames with the UServer. The `UMiddlewares` is a small number of middleware functions that will help you with some operation. 

More specifically the `UMiddlewares` comes with the below predifined functions,
```
BodyParser        -> Checks if the body of the request is type json.
ParamValidation   -> Checks if the url_params are correct.
EnableCors        -> Adds a cors header in the HTTP request. The flag is set to (*) by default
RequestLog        -> Logs every request that happens on the coresponding funvtion.
```

> More middlewares will be added over the time as this library gets bigger. 

### Middleware Setup

A middleware must have the below signature,
```python
def intercept(req, res):
    # ...
    return True
```

As you can see we need to have two parameters. The first one will be the request and the second must be the response. More about those two you can find [here](#request). If you want to continue to the next middleware you need to return True on the function, if not you dont need to return anything.

If you would like to raise an `Exception` you can do it like this,
```python
def intercept(req, res):
    # ...
    return Exception('error message')
```

You just need to return an `Exception` with a message. The client will recieve the next json response,
```
Output: 
{
    error: 'error message'
}
```

### Error Overriding

If you dont like this error response message you can change it with the next commands,
```python
@app.error.override()
def error(req, res):
    # Your code ..
```

You have to simple add a `@app.error.override` over your function.

### Middleware Queue

If we have the next section of code,
```python
@app.router.post('/person', middlewares=[BodyParser, ParamValidation, intercept])
def create_person(req, res):
    pass
```

The first middleware that will be executed will be the middleware on the zero index. More specifically,
```
BodyParser -> ParamValidation -> intercept -> create_person
```
