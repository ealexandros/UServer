# UServer Testing ![micropython](https://img.shields.io/badge/micropython-blue)

*The test will continue to grow as the application gets larger.*

## 📚 Table of Content

- [Description](#-description)
- [Setup](#-setup)
    -[Step 1](#step-1)
    -[Step 2](#step-2)
- [Already Tested](#-already-tested)
- [Conclusion](#-conclusion)

## 🎯 Description

In this subfolder are all the different type of tests that have been used to make sure the package runs smoothly. The tests are made with the help of `unittest2`. They are runned on a local computer, not on a microcontroller like `esp32|8266`.

As metioned above the test will continue to grow as the application gets larger.

## 📦 Setup

### Step 1

In order to run the test you will have to download one python package. This package is called `unittest` and can be downloaded with the next command,
```python
> pip install unittest2
```

### Step 2

Because of the fact that we are running the tests on our local computer you need to replcae the `UServer` file with the `UServerTests` one. More clearly,

##### Windows
```
..\tests> move LocalTestFiles\UServerTests.py ..\src\UServer.py
```

##### Linux
```
..\tests> mv LocalTestFiles/UServerTests.py ../src/UServer.py
```

This will override the hole file. Make sure you have a copy of `UServer`.

## ✅ Already Tested

| Files                     | Description   |
| ------------------------- |---------------------|
| BasicRequestsTests        | Tested the basic functionality of the application. |
| BodyParamsTests           | Tested the request body and the request parameters of the client. |
| MultiPathRequestsTests    | Tested the star **\*** path and some variations with the url parameters. |
| RequestVariableTests      | Tested the request class variables. |
| ResponseBodyTypesTests    | Tested all the different response body types. |

## ✨ Conclusion

Testing helped me a lot with problems I would not even look at. More tests will come over the time. 😋