#!/usr/bin/env python3
"""
Class file for Employee
"""
import random
from datetime import date

class Employee():
    """
    Class for Employee
    """

    def __init__(self, firstname, lastname, salary, hired, id_number=None):
        """
        init method
        """
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.hired = hired # "YYYY-MM-DD"
        self.id_number = id_number if id_number else random.sample(range(10), 4)

    def get_salary(self):
        """
        Returns the salary
        """
        return self.salary

    def get_id(self):
        """
        Returns the employement id
        """
        return "".join(map(str, self.id_number))

    def get_name(self):
        """
        Returns name
        """
        return self.firstname + " " + self.lastname

    def get_days_hired(self):
        """
        Returns the number of days an Employee
        has been hired.
        """
        today = date.today()

        hired_date_list = [int(x) for x in self.hired.split('-')]
        hired_date = date(*hired_date_list)
        # Samma kod fast utan list comprehension:
        # hired_date_list = []
        # for x in self.hired.split('-'):
        #   hired_date_list.append(int(x))
        # * innan listan säger att varje element skall skickas som ett eget argument.
        # hired_date = date(
        #    hired_date_list[0], # År
        #    hired_date_list[1], # Månad
        #    hired_date_list[2], # Dag
        # )

        difference = today - hired_date
        return difference.days

    def to_json(self):
        """
        Returns a dict all the data of an employee
        """
        return {
            "fname": self.firstname,
            "lname": self.lastname,
            "salary": self.salary,
            "hired": self.hired,
            "id": self.id_number,
        }
    # factory method
    @classmethod
    def from_json(cls, json):
        """
        Creates a new instance of the class employee.
        """
        return cls(json["fname"], json["lname"], json["salary"], json["hired"], json["id"])
