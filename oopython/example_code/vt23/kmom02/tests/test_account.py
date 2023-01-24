#!/usr/bin/env python3
""" Module for testing the class Account """

import unittest
import random
from src.account import Account

class TestAccount(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Setup that runs before every testcase """
        random.seed("account")

    def test_create_account_owner_ok(self):
        """ Test if the account is created and owner is correct """
        my_account = Account(10000, "löning", "Marie") # Act
        self.assertEqual(my_account.owner, "Marie", "Check owner is Marie") # Assert
        self.assertNotEqual(my_account.owner, "Andreas") # Assert

    def test_create_account_instance_ok(self):
        """ Test if the account is created and if it is the correct instance """
        my_account = Account(10000, "löning", "Marie") # Act
        self.assertIsInstance(my_account, Account) # Assert

    def test_create_account_name_ok(self):
        """ Test if the account is created and name is correct """
        my_account = Account(10000, "löning", "Marie") # Act
        self.assertIsNotNone(my_account.name, "Account name should not be empty") # Assert

    def test_create_account_number_ok(self):
        """ Test if the account is created and account number is set ok """
        my_account = Account(10000, "löning", "Marie") # Act
        self.assertEqual(my_account.number, 7133616, "Check account number") # Assert

    def test_create_2_accounts_ok(self):
        """ Test if the second account has different account number from the first one. """
        my_account = Account(10000, "löning", "Marie") # Act
        my_account2 = Account(500, "välgörenhet", "Marie") # Act
        self.assertNotEqual(my_account.number, my_account2.number) # Assert

    def test_withdraw_ok(self):
        """ Test if withdraw works """
        my_account = Account(10000, "löning", "Marie") # Act
        res = my_account.withdraw(1000)
        self.assertEqual(my_account.get_balance(), 9000, \
            "Balance after withdraw should be 9000") # Assert
        self.assertTrue(res, "Should be true since ok withdraw") # Assert

    def test_withdraw_not_ok(self):
        """ Test if withdraw work when too large amount is withdrawn """
        my_account = Account(10000, "löning", "Marie") # Act
        res = my_account.withdraw(99000)
        self.assertEqual(my_account.get_balance(), 10000, \
            "Balance the same, 10000, since not ok withdraw") # Assert
        self.assertFalse(res, "Should be false since try to withdraw more than on account") # Assert

    def test_add_method_with_object_ok(self):
        """ Test if add method works as intended with object """
        my_account = Account(10000, "löning", "Marie") # Act
        bonus = Account(1000, "", "") # Act
        new_balance = my_account + bonus
        self.assertEqual(new_balance, 11000, "Balance should be 11000") # Assert

    def test_add_method_with_amount_ok(self):
        """ Test if add method works as intended with amount (integer) """
        my_account = Account(10000, "löning", "Marie") # Act
        new_balance = my_account + 500
        self.assertEqual(new_balance, 10500, "Balance should be 11000") # Assert

    def test_add_method_with_string_ok(self):
        """ Test if add method works as intended with string """
        my_account = Account(10000, "löning", "Marie") # Act
        new_name = my_account + " BTH"
        self.assertEqual(new_name, "löning BTH", "name should be löning BTH") # Assert
        self.assertIn("BTH", new_name, "BTH ska finnas i det nya kontonamnet") # Assert
