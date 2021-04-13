@echo off

set num_arg=0
for %%x in (%*) do Set /A num_arg += 1

if NOT %num_arg%==2 echo Invalid number of args.
if NOT %num_arg%==2 exit

if %1==-e echo Adding ../example
if %1==-e ampy -p %2 -b 115200 put ..\example /

if %1==-l echo Adding ../src
if %2==-l ampy -p %2 -b 115200 put ..\src /lib/
