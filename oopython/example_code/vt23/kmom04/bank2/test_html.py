#!/usr/bin/env python3
"""
Main program for testing with generated html reports
"""
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from tests.test_account import TestAccount
from tests.test_account_magic import TestAccountMagic

if __name__ == '__main__':
    account_tests = TestLoader().loadTestsFromTestCase(TestAccount)
    account_magic_tests = TestLoader().loadTestsFromTestCase(TestAccountMagic)

    kwargs = {
        "verbosity": 2,
        "output": "test_account",
        "report_name": "my_report",
        "report_title": "Testing TestAccount",
        "failfast": False
    }
    runner = HTMLTestRunner(**kwargs)
    runner.run(TestSuite([account_tests]))

    kwargs = {
        "verbosity": 2,
        "output": "test_account_magic",
        "report_name": "my_report_magic",
        "report_title": "Testing TestAccountMagic",
        "failfast": False
    }
    runner = HTMLTestRunner(**kwargs)
    runner.run(TestSuite([account_magic_tests]))
