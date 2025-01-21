#!/usr/bin/env python3
"""
Module for testing the class Account
"""

import unittest
import random

from src.account import Account

class TestAccount(unittest.TestCase):
    """ 
    TestAccount inherits from unittest.TestCase and extends its functionality
    with testcases.
    Testing functionality in the class Account
    """

    def setUp(self): # 
        """ Setup that runs before every testcase """
        random.seed("account")
    
    def test_create_account_owner_ok(self):
        """ Test if the account is created correct owner """
        my_account = Account(10000, "löning", "Marie") # Arrange & Act
        self.assertIsInstance(my_account, Account, "Class should be Account")
        self.assertIsNotNone(my_account.owner, "Check account owner should not be none") # Assert
        self.assertNotEqual(my_account.owner, "", "Check account owner should not be empty") # Assert
        self.assertEqual(my_account.owner, "Marie", "Check account owner") # Assert

    def test_create_account_name_ok(self):
        """ Test if the account is created correct name """
        my_account = Account(10000, "löning", "Marie") # Arrange & Act
        self.assertIsNotNone(my_account.name, "Check account name should not be none") # Assert
        self.assertNotEqual(my_account.name, "", "Check account name should not be empty") # Assert
        self.assertEqual(my_account.name, "löning", "Check account name") # Assert

    def test_create_account_balance_ok(self):
        """ Test if the account is created correct amount >= 0 """
        my_account = Account(10000, "löning", "Marie") # Arrange & Act
        self.assertTrue(my_account.get_balance() >= 0, "Check account balance should be larger or equal to 0.") # Assert
        self.assertEqual(my_account.get_balance(), 10000, "Balance should be 10000.")

    def test_create_account_number_ok(self):
        """ Test it the account number is a valid number """
        my_account = Account(10000, "löning", "Marie") # Arrange & Act
        self.assertTrue(my_account.number >= 1000000, "Check account number should be larger or equal to 0.") # Assert
        self.assertTrue(my_account.number <= 20000000, "Check account number should be larger or equal to 0.") # Assert

    @unittest.skip("Test is redundant. Functionality tested in test_create_account_number_seed_alt_ok.")
    def test_create_account_number_seed_ok(self):
        """ Test it the account number with seed number """
        my_account = Account(10000, "löning", "Marie") # Arrange & Act
        self.assertEqual(my_account.number, 7133616, "Check account number should be seed value 7133616.") # Assert
        my_account = Account(10000, "löning", "Marie2") # Arrange & Act
        self.assertEqual(my_account.number, 5911104, "Check account number should be seed value 5911104.") # Assert
        my_account = Account(10000, "löning", "Marie3") # Arrange & Act
        self.assertEqual(my_account.number, 3162756, "Check account number should be seed value 3162756.") # Assert

    def test_create_account_number_seed_alt_ok(self):
        """ Test it the account number with seed number """
        seed_numbers = [ 7133616, 5911104, 3162756 ]
        my_account = Account(10000, "löning", "Marie") # Arrange & Act
        self.assertEqual(my_account.number, seed_numbers[0], "Check account number should be seed value seed_numbers[0]") # Assert
        my_account = Account(10000, "löning", "Marie2") # Arrange & Act
        self.assertEqual(my_account.number, seed_numbers[1], "Check account number should be seed value seed_numbers[1]") # Assert
        my_account = Account(10000, "löning", "Marie3") # Arrange & Act
        self.assertEqual(my_account.number, seed_numbers[2], "Check account number should be seed value seed_numbers[2]") # Assert

    def test_balance_after_withdraw_ok(self):
        """ Test it the account balance after withdraw has decreased  """
        my_account = Account(10000, "löning", "Marie") # Arrange 
        my_account.withdraw(500) # Act
        self.assertEqual(my_account.get_balance(), 9500, "Balance should be 9500.") # Assert

    def test_balance_after_withdraw_not_ok(self):
        """ Test it the account balance after to large withdraw """
        my_account = Account(10000, "löning", "Marie") # Arrange 
        result = my_account.withdraw(50000) # Act
        self.assertFalse(result, "Withdraw not allowed, should return false.") # Assert
        self.assertEqual(my_account.get_balance(), 10000, "Balance should be the same, 10000.") # Assert

    def test_balance_after_deposit_ok(self):
        """ Test it the account balance after deposit has increased """
        my_account = Account(10000, "löning", "Marie") # Arrange 
        my_account.deposit(500) # Act
        self.assertEqual(my_account.get_balance(), 10500, "Balance should be 10500.") # Assert

    def test_balance_after_deposit_not_ok(self):
        """ Test it the account balance after deposit with a negative number is the same """
        my_account = Account(10000, "löning", "Marie") # Arrange 
        result = my_account.deposit(-500) # Act
        self.assertFalse(result, "Deposit not allowed, should return false.") # Assert
        self.assertEqual(my_account.get_balance(), 10000, "Balance should be the same, 10000.") # Assert
