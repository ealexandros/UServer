# Documentation ![version](https://img.shields.io/badge/version-1.1.0-brightengreen)

In **README.md** file you wil find the complete documentation of the `UServer` repository. This file may be chnaged over the time, because more functionality will be added to the project.

So lets start!

## 📚 Table of Content

- [Boot](#-bootpy)
    - [ENV](#env-module)
    - [ENV tutorial](#how-env-works)
- [Setup](#-setuppy)
    - [Basic Setup](#basic-setup)
    - [Routes](#routes)
    - [Functions](#functions)
        - [Request](#request)
        - [Response](#response)
    - [HTML Parameters](#html-Parameters)
    - [Paths and Redirects](#paths-and-redirects)
    - [URL Params](#url-params)
    - [App Start](#app-start)
- [Middlewares](#-middlewarespy)
    - [UMiddlewares.py](#umiddlewares.py)
    - [Middleware Setup](#middleware-setup)
    - [Error Overriding](#error-overriding)
    - [Middleware Queue](#middleware-queue)
- [Static](#-staticpy)
    - [Basic Setup](#basic-setup)
    - [Static Example](#static-example)
    - [Static Paths](#static-paths)
- [Documentation](#-documentationpy)
    - [Default Documentation](#default-documentation)
        - [Method 1](#method-1)
        - [Method 2](#method-2)
        - [Method Conflict](#method-conflict)
    - [Documentation Path](#documentation-path)
    - [JSON Documentation](#json-documentation)
- [Restful](#-restfulpy)
    - [Basic Structure](#basic-structure)
    - [Class Parameters](#class-parameters)
- [Conclusion](#-conclusion)

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
@app.router.head(*path*)
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
1. res.send_plain(*data*, *extra_headers*)                       ->  sends plain text.
2. res.send_json(*data*, *extra_headers*)                        ->  sends json.
3. res.send_html(*data*, *extra_headers*, *path*, *args*)        ->  sends html.
4. res.send_css(*data*, *extra_headers*, *path*, *args*)         ->  sends css.
5. res.send_javascript(*data*, *extra_headers*, *path*, *args*)  ->  sends jsvascript.
6. res.send_xml(*data*, *extra_headers*)                         ->  sends xml.
7. res.cors(*cors_flag*)                                         ->  adds cors header flag.
```

All of the above methods can take extra headers. the headers **must** be an object. For example,

```python
headers = {
    'Content-Type': 'text/css',
    'Server': 'ESP'
}
```

In the `res.send_html`, `res.send_css` and `res.send_javascript` methods there is a parameter called *path*. The path parameter is set by default to `False`, if it is set to `True` then instead of passing the html, css or javascript file directly, pass the path to the file and it will automatically open the file. For example,
```python
res.send_html('/path/to/index.html', path=True)
```

### HTML Parameters

One more thing to mention is that at `send_html`, `send_css` and `send_javascript` in the response, there is an **args** parameter. This **args** parameter passes parameters to your html code.
In order to pass the parameters to the html code, there needs to be a `%name%` string in the html code. For example,
```html
<body>
    <h1>%test%</h1>
</body>
```

After adding the `%test%` string to the html simply pass a parameter to the `res.send_html()` like this,
```python
res.send_html('''
    <body>
        <h1>%test%</h1>
    </body>
''', test='your value')
```

The response will be the next,
```
Output: 
    <body>
        <h1>your value</h1>
    </body>
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

If you want every path to redirect to your functions you just need to add `*` in your path. For example,
```python
@app.router.get('/', redirects=['*'])
def index(req, res):
    # ..Business Logic
    res.send('All good')
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

For a better understanding of the middlewares in the userver package you can see the [middlewares.py](https://github.com/alexandros44/UServer/blob/main/examples/setup.py) file. Lets start to analyze that file.

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

## 🗄 Static.py

For a better understanding of the auto-documentation in the userver package you can see the [static.py](https://github.com/alexandros44/UServer/blob/main/examples/static.py) file. Lets see how everything works.

### Basic Setup

The package comes with a function called `static`. This function publishes all your static html/css, javascript, images etc inside your specified folder. In order for it to work this must be executed,
```python
app.static("folder_path")
```

The `folder_path` must be the absolute path to the folder.

### Static Example

If you have a subfolder in your project like this,
```
./YourProject
├── static/
│   ├── style/
│   │   └── style.css
│   ├── js/
│   │   └── index.js
│   ├── index.html.py
│   ├── login.html.py
│   └── about.html.py
├── main.py
└── boot.py
```
You can publish the hole folder with the next commant inside the main file,

```python
app.static("static")
```

P.S: Even files inside subdirectories will be published.

### Static Paths

In order to access the published files first of all we need to use the folder path as a prefix. If we use the previous example we will have the next,
```
http://xxx.xxx.xxx.xxxx:pppp/static/index.html
http://xxx.xxx.xxx.xxxx:pppp/static/login.html
http://xxx.xxx.xxx.xxxx:pppp/static/about.html
http://xxx.xxx.xxx.xxxx:pppp/static/style/style.css
http://xxx.xxx.xxx.xxxx:pppp/static/js/index.js
```

The `x` indicates the IP address and the `p` indicates the port of the applicaiton.

## 📃 Documentation.py

For a better understanding of the auto-documentation in the userver package you can see the [documentation.py](https://github.com/alexandros44/UServer/blob/main/examples/documentation.py) file. Lets see how everything works.

### Default Documentation

The documentation will be generates based on the routes you already gave. For exmple if we have the code below,
```python
@app.router.post(*path*)
def create_(req, res):
    # ..Business Logic..
    pass
```

#### Method 1

The `POST` path will be added to the documentation. If you would like to add a description to that path and the response codes that may be returned you can do it like this,
```python
@app.router.post('/person', middlewares=[EnableCors],
    description="You can create a new person by creating a json file with the `username`, `fnmae`, `password` and the `email`",
    return_codes={
        '200': 'person created',
        '404': 'json does not contain all the necessary fields',
        '409': 'person exist need to change email or password'
    })
def create_(req, res):
    # ..Business Logic..
    pass
```

Simply add two extra parameters on the decorator function. (description,  return_codes)

1. The **description** must be a string type parameter.
2. The **return_codes**, must be an object type parameter.

#### Method 2

For the second method you can simply write the documentation like the go below,
```python
@app.router.delete('/person/:id', docs=
    '''
        description: ... 
        ...
        ...

        return_codes: {
            "200": "person deleted",
            "400": "not authorized"
        }
    ''')
def delete_person(req, res):
    url_id = req.get_url('id')
    res.send_json({ 'id': url_id })
```

As you can see you have to add a `docs` parameter to the methods decorator. First you need to add the description and afterwards the return_codes. The description can be a string on multiple lines. The return_codes on the other hand must be in `json` format. It must consist of `"` and `,` after every entry. You can take a better look [here](https://en.wikipedia.org/wiki/JSON).

#### Method Conflict

If both methods are implemented, the second method will override the first method. For example if we have something like this,
```python
@app.router.delete('/person/:id', description=".", return_codes={ '100': 'this will not show' }, docs=
    '''
        description: ...

        return_codes: { "200": "person deleted" }
    ''')
def delete_person(req, res):
    url_id = req.get_url('id')
    res.send_json({ 'id': url_id })

```

The auto documentation will select the,
```
description = ...
return_codes = { "200": "person deleted" }
```

### Documentation Path

If you want to show the documentation you just need to go to your browser and type the IP address and the port of the host and then add the `/docs` path. More specifically,
```
http://xxx.xxx.xxx.xxx:port/docs
```

The `/docs` is the default path for the documentation. You can change it by changing the `doc_path` in the app.start().
```python
app.start(logger=True, doc_path='/test/docs')
```

If you would like to disable the auto documentation you can do that by changing the parameter `show_doc`in the app.start()
```python
app.start(logger=True, show_doc=False)
```

### JSON Documentation

One more thing to mention is that after the path of the documentation (by default the `/docs`) we have another path with the documentation in json. That path serves the auto documentation in json format. You can look below to understand better the paths,
```
http://xxx.xxx.xxx.xxx:port/docs        ->  default auto documentation html
http://xxx.xxx.xxx.xxx:port/docs/json   ->  default auto documentation json
```

## 💫 Restful.py

For a better understanding of the auto-documentation in the userver package you can see the [restful.py](https://github.com/alexandros44/UServer/blob/main/examples/restful.py) file. Lets see how everything works.

### Basic Structure

Until now if you would like to add to your `http://localhost:3000/user` url the methods `GET`, `POST` and the `DELETE` you would have to do it like this,
```python
@app.router.get('/user')
def get_person(req, res):
    # ..Business Logic.. #
    res.send()

@app.router.post('/user')
def create_person(req, res):
    # ..Business Logic.. #
    res.send()

@app.router.delete('/user')
def delete_person(req, res):
    # ..Business Logic.. #
    res.send()
```

That is not a but implementation but there is a more simple one. You can use the `@app.router.restful(*path*)` method which comes with the `userver` package. In the previous example we can write it now like this,
```python
@app.router.restful('/user')
class User:
    def get(self, req, res):
        # ..Business Logic.. #
        res.send()
        
    def post(self, req, res):
        # ..Business Logic.. #
        res.send()

    def delete(self, req, res):
        # ..Business Logic.. #
        res.send()
```

The `@app.router.restful` takes the same parameters as the `app.router.*` methods.

### Class Parameters

If we want the `User` class to have a constructor with parameters, for example,
```python
@app.router.restful('user')
class User:
    def __init__(self, param):
        self.param = param

    def get(self, req, res):
        # ..Business Logic.. #
        res.send()
```

There is a special parameter in the `@app.router.restful()` decorator which takes as an input a tuple. The parameter `class_args=`. The above example would throw an `Exception` because the class expects an argument. The correct way would be,
```python

@app.router.restful('user', class_args=('100'))
class User:
    def __init__(self, param):
        self.param = param

    def get(self, req, res):
        # ..Business Logic.. #
        res.send(self.param)
```

Afterwards this parameter `self.param` can be used inside the `get` method.

## ✨ Conclusion

This `README.md` file covers all of the functionality of this repository. Over the time this file will be updated with new stuff as the repository grows.
