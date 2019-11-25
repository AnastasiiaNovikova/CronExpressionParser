# coding: utf-8
import re
import sys
from collections import OrderedDict

from exception import CronExpressionParserError


class CronExpressionParser:
    """
    Class to parse cron string and expand each field to show the times at which it will run
    """

    def __init__(self, command):
        self.cron_command = command
        self.param_names = ["minute", "hour", "day of month", "month", "day of week"]
        self.param_ranges = {
            "minute": range(60),
            "hour": range(24),
            "day of month": range(1, 32),
            "month": range(1, 13),
            "day of week": range(1, 8),
        }
        self.output_name_length = 14

    def get_range(self, param, value):
        """
        Function takes cron parameter with its value and returns the time range at which it will run
        """
        digits = re.findall(r"\d+", value)
        range_for_value = self.param_ranges[param]
        if not all([int(item) in range_for_value for item in digits]):
            raise CronExpressionParserError(
                CronExpressionParserError.ERROR_VALUE_OUT_OF_RANGE
            )
        elif value.isdigit():
            return value
        elif "," in value:
            return " ".join(value.split(","))
        elif "/" in value:
            div = int(value.split("/")[1])
            return " ".join([str(item) for item in range_for_value if item % div == 0])
        elif "*" in value:
            return " ".join(map(str, range_for_value))
        elif "-" in value:
            start, end = map(int, value.split("-"))
            return " ".join(
                [str(item) for item in range_for_value if start <= item <= end]
            )
        else:
            raise CronExpressionParserError(
                CronExpressionParserError.ERROR_WRONG_COMMAND_FORMAT
            )

    def print_result(self, result):
        """
        Function prints result to standard output
        """
        for key, value in result.items():
            whitespaces = " " * (self.output_name_length - len(key))
            sys.stdout.write("{}{}{}\n".format(key, whitespaces, value))

    def parse_cron_command(self):
        """
        Function converts cron string to dict in which key is the name of the parameter
        and the value is the value from the input string
        """
        *params, command = self.cron_command.split()

        if len(params) != 5:
            print("wrong number af arguments")
            raise CronExpressionParserError(
                CronExpressionParserError.ERROR_WRONG_NUMBER_OF_ARGUMENTS
            )

        cron_command_dict = OrderedDict()
        for param, value in zip(self.param_names, params):
            cron_command_dict[param] = self.get_range(param, value)
        cron_command_dict["command"] = command

        return cron_command_dict


if __name__ == "__main__":
    try:
        cron_expression = sys.argv[1]
    except IndexError:
        raise CronExpressionParserError(
            CronExpressionParserError.ERROR_COMMAND_NOT_PROVIDED
        )

    cron_expression_parser = CronExpressionParser(cron_expression)
    parsed_expression = cron_expression_parser.parse_cron_command()
    cron_expression_parser.print_result(parsed_expression)
