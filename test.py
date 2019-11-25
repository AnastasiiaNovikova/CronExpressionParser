# coding: utf-8
import unittest

from cron_expression_parser import CronExpressionParser
from exception import CronExpressionParserError


class TestCronExpressionParser(unittest.TestCase):
    """
    Class to test CronExpressionParser
    """

    def test_parse_cron_command_ok(self):
        """
        Test checks different correct variants of input parameters
        """
        cron_command = "*/15 0 1,15 * 1-5 /usr/bin/find"
        cron_expression_parser = CronExpressionParser(cron_command)
        result = cron_expression_parser.parse_cron_command()
        true_result = {
            "minute": "0 15 30 45",
            "hour": "0",
            "day of month": "1 15",
            "month": "1 2 3 4 5 6 7 8 9 10 11 12",
            "day of week": "1 2 3 4 5",
            "command": "/usr/bin/find",
        }
        self.assertDictEqual(result, true_result)

    def test_parse_errors(self):
        """
        Test checks basic parsing error cases
        """
        wrong_format_commands = [
            "*/15 0 1,15 * 1-8 /usr/bin/find",  # wrong day of week range
            "*/15 0 1,15 * 1-5",  # wrong number of arguments
            "*/15 0 1,15 * 1&5 /usr/bin/find",  # wrong symbols in day of week parameter
        ]
        for command in wrong_format_commands:
            cron_expression_parser = CronExpressionParser(command)
            with self.assertRaises(CronExpressionParserError):
                cron_expression_parser.parse_cron_command()


if __name__ == "__main__":
    unittest.main()
