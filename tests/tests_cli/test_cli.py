import os

from pyscholar import cli
import unittest
from click.testing import CliRunner

from pyscholar.config.config import Config


class CliTestCase(unittest.TestCase):

    def test_main(self):
        self._status_and_msg(0, 'main')
        self._status_and_msg(0, '--help  Show this message and exit.', ['--help'])

    def test_storage_strategy_border_cases(self):
        self._status_and_msg(0, '--help  Show this message and exit.', ['storage'])
        self._status_and_msg(2, 'Error: Missing argument "NAME"', ['storage', 'set_strategy'])
        self._status_and_msg(0, '--help  Show this message and exit.', ['storage', 'set_strategy', '--help'])

    def test_storage_strategy_happy_path(self):
        runner = CliRunner()
        storage_result = runner.invoke(cli.main, ['storage', 'set_strategy', 'some_value'])
        self.assertEqual(storage_result.exit_code, 0)
        config = Config(str(os.system("echo $(pwd)")) + 'config_test.ini')
        self.assertEqual('some_value', config.get('storage', 'strategy'))

        storage_result = runner.invoke(cli.main, ['storage', 'set_strategy', 'csv_strategy'])
        self.assertEqual(storage_result.exit_code, 0)
        config = Config(str(os.system("echo $(pwd)")) + 'config_test.ini')
        self.assertEqual('csv_strategy', config.get('storage', 'strategy'))

    def test_storage_file_name_border_cases(self):
        self._status_and_msg(0, '--help  Show this message and exit.', ['storage'])
        self._status_and_msg(2, 'Error: Missing argument "NAME"', ['storage', 'file_name'])
        self._status_and_msg(0, '--help  Show this message and exit.', ['storage', 'file_name', '--help'])

    def test_storage_file_name_happy_path(self):
        runner = CliRunner()
        storage_result = runner.invoke(cli.main, ['storage', 'file_name', 'results.csv'])
        self.assertEqual(storage_result.exit_code, 0)
        config = Config(str(os.system("echo $(pwd)")) + 'config_test.ini')
        self.assertEqual('results.csv', config.get('storage', 'file_name'))

    def _status_and_msg(self, expected_status, expected_msg, cmd=None, error_msg=None):
        runner = CliRunner()
        storage_result = runner.invoke(cli.main, cmd) if cmd is not None else runner.invoke(cli.main)
        self.assertEqual(storage_result.exit_code, expected_status, error_msg)
        self.assertTrue(expected_msg in storage_result.output, error_msg)


if __name__ == '__main__':
    unittest.main()
