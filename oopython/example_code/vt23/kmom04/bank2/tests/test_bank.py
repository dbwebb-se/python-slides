#!/usr/bin/env python3
"""
Class for testing the Bank class
"""
import unittest
from unittest import mock
from unittest.mock import patch
from unittest.mock import Mock

from src.bank import Bank
from src.account import Account

class TestBank(unittest.TestCase):
    no_of_customers = mock.MagicMock
    no_of_customers.return_value = 10

    def test_number_of_customers_is_zero(self):
        ''' When creating the bank the number of customers should be 0'''
        b = Bank([]) # Arrange and Act
        self.assertEqual(len(b.owners), 0) # Assert

    def test_number_of_customers(self):
        ''' After get owner from the database the customers should be 10'''
        b = Bank() # Arrange
        with patch.object(Bank, 'get_owners', return_value=10): # Act
            self.assertEqual(b.get_owners(), 10)  # Assert

    def test_number_of_accounts_for_existing_customer(self):
        ''' Get accounts from customer Andreas, should be 2 accounts '''
        b = Bank() # Arrange 
        accounts = [Account(100, "räntor", "Andreas"), Account(20, "lån", "Andreas")] # Arrange 
        with patch.object(Bank, 'get_account_from_owner', return_value=accounts): # Act
            self.assertEqual(len(b.get_account_from_owner()), 2)  # Assert

    def test_number_of_accounts_for_nonexisting_customer(self):
        ''' Get accounts from customer Marie, should be 0 accounts, since Marie is not a customer in the bank '''
        b = Bank() # Arrange
        accounts = [] # Arrange
        mock_bank = Mock()  # Arrange
        mock_bank.get_account_from_owner = Mock(accounts)  # Act
        self.assertEqual(b.get_account_from_owner(mock_bank), [])  # Assert