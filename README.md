# Welcome to Gift Store!
This is where you can start to get familiar with the problem and what you need to run it.
This codebase is used during code pairing session for JOI initiative.
It's focused on identifying code smells, refactoring and testing legacy codebase while promoting conversations.

## Problem Statement
A college student with a group of friends enjoys giving gifts tailored to each person's interests. He/She frequents a gift shop that offers a wide range of transaction. Could you assist him/her in calculating his/her expenditure on gifts?
5% GST gets added on total worth of products.<br>
NOTE1:- Make sure to handle exceptions gracefully.<br>
NOTE2:- Make sure to write modular code.<br>
For more info refer to the problem statement document shared to you separately.

## Technology used
- Python
- unittest - unit testing framework

## Before the interview
Get familiar with the codebase! Make sure you have the necessary dependencies installed, and that you are able to run the tests.

## Setup
```console
source ./start
```

## Run Tests
```console
python -m unittest
```

## Done
```console
source ./done && deactivate
```

## Run the Sample Application
To understand how this library would be used you can check the `main` method in the `Application.py`. If you want to see the results, run:
```console
python Application.py
```

## Existing Implementation
Application code currently has the following implementation:
- Required Domain Models needed for the base problem statement.
- Hard-coded list of gift items with their prices.
- A function to calculate the total cost of gifts (stubbed to add the core logic on your own).