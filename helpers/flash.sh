#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo Invalid number of parameters.
    exit
fi

if [ "$1" == "-e" ]; then
    echo Adding ../examples into micropython
    ampy -p "$2" put ..\example /
elif [ "$1" == "-l" ]; then
    echo Adding ../src into micropython
    ampy -p "$2" put ..\src /lib/
fi