''' Comment '''

import unittest
from unittest.mock import Mock
from unittest import TestCase

class CarShop:
    ''' Comment '''
    @staticmethod
    def get_owner_info(a_obj, reg_number):
        ''' Comment '''
        return a_obj.get_info(reg_number)

class TestCar(TestCase):
    ''' Comment '''
    def test_get_owner_info(self):
        ''' Comment '''
        shop = CarShop()
        mock = Mock()
        mock.get_info = Mock(return_value="Marie")

        print(self.assertEqual(shop.get_owner_info(mock, "ABC 123"), "Marie"))

if __name__ == '__main__':
    unittest.main()
