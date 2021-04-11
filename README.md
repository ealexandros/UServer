# UServer

*This is a micropython HTTP web server repository.*

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

**P.S**: Some `regex` functions like are not included in the `re` library in micropython so there is an additional class in [./src/helpers/RegexHelpers]() for all the missing ones.
 
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
.\Userver> .\flash.bat -l *communicaiton_port*
```

##### Linux
```bash
.\Userver> ./flash -l *communicaiton_port*
```

Where the communication port is the port in which your microcontroller is connected.

**P.S**: First make sure that you downloaded all the necessary tools. (Check the [requirements](#-requirements) for more)

## 📃 Documentation

## ✨Conclusion
