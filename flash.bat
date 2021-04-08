@echo off

set num_arg=0
for %%x in (%*) do Set /A num_arg += 1

if NOT %num_arg%==2 echo Invalid number of args.
if NOT %num_arg%==2 exit

if %2==0 echo Adding ./example
if %2==0 ampy -p %1 -b 115200 put .\example /

if %2==1 echo Adding ./src
if %2==1 ampy -p %1 -b 115200 put .\src /lib/
