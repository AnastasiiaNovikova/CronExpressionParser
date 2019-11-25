# coding: utf-8
class CronExpressionParserError(Exception):
    ERROR_COMMAND_NOT_PROVIDED = "Cron command was not provided"
    ERROR_VALUE_OUT_OF_RANGE = "Input value is not in allowed range"
    ERROR_WRONG_COMMAND_FORMAT = "Wrong command format provided"
    ERROR_WRONG_NUMBER_OF_ARGUMENTS = "Wrong number of arguments"
