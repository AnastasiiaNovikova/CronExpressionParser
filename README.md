# CronExpressionParser

The aim of the project is to parse standard cron string and to expend each field to show the times at which it will run

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python3 installed is necessary to run the code. Assume you have it on your machine. There are no other mandatory requirements but you can install Python style libraries isort and black.

```
pip install -r requirements.txt
```

### Running the code

In order to run the code go to the project folder and run the code with the command

```
python cron_expression_parser.py '*/15 0 1,4 5-6 1,3 usr/bin/find' # '*/15 0 1,4 5-6 1,3 usr/bin/find' is an example of the input cron string
```

## Running the tests

In order to run the tests use the following command

```
python test.py
```

The tests check basic correct input variants and error cases



