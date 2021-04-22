# UServer ![micropytho](https://img.shields.io/badge/micropython-blue) ![version](https://img.shields.io/badge/version-1.1.0-brightengreen)

*This is a micropython HTTP web application server repository.*

## 📚 Table of Content

- [Description](#-description)
- [Setup](#-setup)
    - [First Step](#step-1)
    - [Second Step](#step-2)
- [Requirements](#-requirements)
- [Documentation](#-documentation)
- [Conclusion](#-conclusion)
 
## 🎯 Description

Inside this repository you will find a HTTP web server compatable with micropython. You can set the request type(s) you want to listen and send the right responses. For more informations about the capabilities of the library you can peek at the [documentation](#-documentation).


#### The project was made with the help of:

1. **Sockets**, which helped me with the web API.
2. **Regex**, which helped me with finding patterns in strings. 

**P.S**: Some `regex` and `os` functions like **findall**, **walk** etc, are not included in the base libraries in micropython, so there is an additional files in [./src/helpers/RegexHelpers.py](https://github.com/alexandros44/UServer/blob/main/src/helpers/RegexHelpers.py) and [./src/helpers/OSPath.py](https://github.com/alexandros44/UServer/blob/main/src/helpers/OSPath.py) for the implamentation of them.
 
## 📦 Requirements

For starters you will need to have micropython installed on your microcontroller. You can find out more about that in [here](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html).

Also you will need to install `python` and `pip`. After installing those run:
```bash
> pip install adafruit-ampy
```

## 🚀 Setup


#### Step 1

For now if you want to use this library you need to clone the repository. You can do that with the help of `git`:
```bash
..> git clone https://github.com/alexandros44/UServer.git
````

#### Step 2

After cloning the repository you need to type the following command:

##### Windows
```bash
.\Userver\helpers> .\flash.bat -l *communicaiton_port*
```

##### Linux
```bash
.\Userver\helpers> ./flash -l *communicaiton_port*
```

The `communication_port` is the port in which your microcontroller is connected.

**P.S**: First make sure that you downloaded all the necessary tools. (Check the [requirements](#-requirements) for more)

## 📃 Documentation

The complete documantation you can find in the [./examples/README.md](https://github.com/alexandros44/UServer/blob/main/examples/README.md) file. There are also some applications that demonstrate how this library works in the `./example` folder. Over the time i will make more of these applications for better understanding. The most essential applications/examples are:

1. **[setup.py](https://github.com/alexandros44/UServer/blob/main/examples/setup.py)**, starts up the server.
2. **[options.py](https://github.com/alexandros44/UServer/blob/main/examples/options.py)**, adding middlewares, logging, etc.
3. **[middlewares.py](https://github.com/alexandros44/UServer/blob/main/examples/middlewares.py)**, creating and added middlewares.


## ✨ Conclusion

This project gave me a lot of new knowledge about the HTTP (HyperText Transfer Protocol). Started it for fun but ended up making it a github repository.

Watch out there might be bugs. If you **find** any let me know. 😋
