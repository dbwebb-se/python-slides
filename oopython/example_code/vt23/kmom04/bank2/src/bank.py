#!/usr/bin/env python3
"""
Bank class
"""

class Bank:
    """
    Represents a bank with owner stored in a database
    """
    def __init__(self, owners=None):
        if owners is None:
            self.owners = self.get_from_database()
        else:
            self.owners = owners

    def get_from_database(self):
        ''' Should get from database '''
        return []

    def get_owners(self):
        return self.owners

    def get_account_from_owner(self, owner):
        account_list = []
        for owner in self.owners:
            if owner.name == owner:
                account_list.append(owner.accounts)
                break
        return account_list