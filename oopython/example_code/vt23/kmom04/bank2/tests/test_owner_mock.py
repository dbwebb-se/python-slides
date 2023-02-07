#!/usr/bin/env python3
"""
Class for testing the Owner class with mock
"""
import unittest
from unittest import mock
import random

from src.owner import Owner
from src.empty_list_exception import EmptyAccountListException
from src.account import Account

class TestOwnerMock(unittest.TestCase):
    """ Test class"""

    def raise_exception(self):
        raise EmptyAccountListException()

    def setUp(self):
        self.owner1 = mock.Mock()
        self.owner1.name = "Andreas"
        self.owner1.address = "BTH"
        self.owner1.side_effect = ["933838339", 2] # SSN and number of accounts
        self.owner2 = mock.Mock()
        self.owner2.name = "Marie"
        self.owner2.address = "BTH"
        self.owner2.side_effect = 0 # Number of accounts
        self.owner2.get_accounts = self.raise_exception 
    
    def test_owner1_ok(self):
        """ Test owner 1, that the data is correct """
        self.assertEqual(self.owner1.name, "Andreas", "Name should be Andreas") # Assert
        self.assertEqual(self.owner1(), "933838339", "SSN should be 933838339") # Assert
        self.assertEqual(self.owner1.address, "BTH", "Address should be BTH") # Assert
        self.assertEqual(self.owner1(), 2, "No of accounts should be 2") # Assert

    def test_owner2_EmptyAccountListException(self):
        """ Test that owner2 gets EmptyAccountListException since no accounts """
        with self.assertRaises(EmptyAccountListException) as _:
            self.owner2.get_accounts()

    def test_owner1_1_account_number_ok(self):
        """ Test that account number is set """
        owner1 = Owner("Andreas", "933838339", "BTH")# Arrange
        with mock.patch.object(random, 'randint') as rand_mock:
            rand_mock.return_value = 7133616
            a1 = Account(100, "räntor", self.owner1) # Arrange
            a2 = Account(35, "aktier", self.owner1) # Arrange
            owner1.accounts.extend([a1, a2]) # Arrange
        accounts = owner1.get_accounts()
        self.assertEqual(accounts[0].number, 7133616)
        self.assertEqual(accounts[1].number, 7133616)
        
    def test_owner1_2_account_number_ok(self):
        """ Test that account number is set """
        owner1 = Owner("Andreas", "933838339", "BTH")# Arrange
        with mock.patch.object(random, 'randint') as rand_mock:
            rand_mock.side_effect = [7133616, 7777777]
            a1 = Account(100, "räntor", self.owner1) # Arrange
            a2 = Account(35, "aktier", self.owner1) # Arrange
            owner1.accounts.extend([a1, a2]) # Arrange
        accounts = owner1.get_accounts()
        self.assertEqual(accounts[0].number, 7133616)
        self.assertNotEqual(accounts[1].number, 7133616)
        self.assertEqual(accounts[1].number, 7777777)

    def test_owner1_1_account_number_another_test_ok(self):
        """ Test that account number is set """
        a1 = Account(100, "räntor", self.owner1)
        a1.number = mock.MagicMock(return_value=7133616)
        a2 = Account(35, "aktier", self.owner1)
        a2.number = mock.MagicMock(return_value=7777777)
        self.owner1.get_accounts.return_value =[a1, a2]
        self.assertEqual(self.owner1.get_accounts()[0].number(), 7133616)
        self.assertEqual(self.owner1.get_accounts()[1].number(), 7777777)

    def test_owner1_1_account_number_another_test_again_ok(self):
        """ Test that account number is set """
        m = mock.MagicMock()
        m.get_accounts.side_effect = [7133616, 7777777]
        self.assertEqual(m.get_accounts(), 7133616)
        self.assertEqual(m.get_accounts(), 7777777)