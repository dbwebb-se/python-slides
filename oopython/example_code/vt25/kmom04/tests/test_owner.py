#!/usr/bin/env python3
"""
Class for testing the Owner class
"""
import unittest
import random

from src.owner import Owner
from src.empty_list_exception import EmptyAccountListException
from src.account import Account

class TestOwner(unittest.TestCase):
    """ Test class"""
    def setUp(self):
        self.owner1 = Owner("Andreas", "933838339", "BTH") # Arrange
        a1 = Account(100, "räntor", self.owner1) # Arrange
        a2 = Account(35, "aktier", self.owner1) # Arrange
        self.owner1.accounts.extend([a1, a2]) # Arrange
        self.owner2 = Owner("Marie", "999888777", "BTH") # Arrange
    
    def test_owner1_ok(self):
        """ Test owner 1, that the data is correct """
        self.assertEqual(self.owner1.name, "Andreas", "Name should be Andreas") # Assert
        self.assertEqual(self.owner1.get_ssn(), "933838339", "SSN should be 933838339") # Assert
        self.assertEqual(self.owner1.address, "BTH", "Address should be BTH") # Assert
        self.assertEqual(len(self.owner1.accounts), 2, "No of accounts should be 2") # Assert

    def test_owner2_no_accounts_ok(self):
        """ Test owner 2, number of accounts should be 0 """
        self.assertEqual(len(self.owner2.accounts), 0, "No of accounts should be 0") # Assert

    def test_owner2_EmptyAccountListException(self):
        """ Test that owner2 gets EmptyAccountListException since no accounts """
        with self.assertRaises(EmptyAccountListException) as _:
            self.owner2.get_accounts()

    def test_owner1_get_accounts_ok(self):
        """ Test that owner1 gets 2 and not EmptyAccountListException """
        self.assertEqual(len(self.owner1.get_accounts()), 2, "No of accounts should be 2") # Assert

    @unittest.skip
    def test_owner1_account_number_ok(self):
        """ Test that account number is set """
        random.seed("account")
        accounts = self.owner1.get_accounts()
        print(accounts[0].number, accounts[1].number)
        self.assertNotEqual(accounts[0].number, 0, "Number should not be 0") # Assert
        self.assertEqual(accounts[0].number, 7133616, "Number should be 7133616") # Assert