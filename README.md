# CronExpressionParser

The aim of the project is to parse a standard cron string and to expand each field to show the times at which it will run

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python3 installed is necessary to run the code. We assume you have it on your machine. There are no other mandatory requirements but you can install Python style libraries isort and black using command:

```
pip install -r requirements.txt
```

In order to run isort use the following command:

```
isort mypythonfile.py mypythonfile2.py
```

In order to run black use the following command:

```
black {source_file_or_directory}
```

Where cron_expression_parser.py is the example of the name of the file

### Running the code

In order to run the code clone the project, and run the following command form the project folder

```
python cron_expression_parser.py '*/15 0 1,4 5-6 1,3 usr/bin/find' 
```
Where '*/15 0 1,4 5-6 1,3 usr/bin/find' is the example of the input cron string

If cron string is not provided or the format of the cron string is wrong an error will be raised

Special time strings such as "@yearly" are not supported

For "day of week" parameter numbers from 1 to 7 are allowed but we don't make 0 and 7 equal variants

For "day of month" parameter we assume that there are 31 days in each month

## Running the tests

In order to run the tests use the following command:

```
python test.py
```

The tests check basic correct input variants and error cases



