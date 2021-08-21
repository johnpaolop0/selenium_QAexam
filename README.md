##QE Exam
_Automation using Selenium with Python._

Scenario
-here are the covered scenario to be test on selenium
- Price Descending
- Price Ascending
- A-Z
- Z-A
- clientWidth

##Instruction 

To run this program the operating system needs to  install Python [download](https://www.python.org/downloads/) and Visual Sutdio Code [download](https://code.visualstudio.com/).

Installed packages
-enter the following package on the terminal after installing python
>pip3 install selenium
>pip3 install webdriver-manager
>pip3 install pytest


##Run the test scenario
open terminal and find the location of the script

-to run all the test scenario enter
>pytest -v -s test_qaexam.py

-to run a single test scenario enter
>pytest -v -s test_qaexam.py::TestQAExam::test_PriceDescending
