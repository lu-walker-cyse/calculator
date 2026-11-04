# Calculator
A simple command line interface for basic calculator functions, built in python3

## What it will do
Add, subtract, multily and divide two numbers; display the result.

## How to run it
Run: "python3 calculator.py"
Enter the first number, operator (+,-,*,/), then second number.
The program prints Result: followed by the answer.

## How to test it
Activate the SCCM4910 virtual environment using:
"source /opt/python-venv/sccm-4910/bin/activate"
Check that pytest exists using:
"python3 -m pytest --version"
Run the test using: "./check.sh"
The expected result is that all five tests pass.
Use "echo $?" to read the exit status immediately after testing
0 means the tests succeeded
1 means there were tests that failed
5 means no test were collected
 
