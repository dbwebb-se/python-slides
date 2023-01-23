#!/usr/bin/env python3 pylint: disable=broad-except

"""
Handler file
"""

import json
from employee import Employee

class Handler():
    """
    Class that handles employees
    """
    filename = "static/data/employees.json"

    def __init__(self):
        """ Constructor """
        self.people = []
        try:
            self.load_data()
        except FileNotFoundError:
            self.add_predefined_employees()
        except Exception:
            self.add_predefined_employees()

    def get_people(self):
        """ Returns people, a list with employees """
        return self.people

    def add_predefined_employees(self):
        """ Adds this predefined employees to people """
        emil = Employee("Emil", "Folino", 30000, "2011-05-13")
        mikael = Employee("Mikael", "Roos", 31000, "2010-01-01")
        kenneth = Employee("Kenneth", "Lewenhagen", 75000, "2019-10-05")
        andreas = Employee("Andreas", "Arnesson", 12000, "2020-03-02")

        self.people.append(emil)
        self.people.append(mikael)
        self.people.append(kenneth)
        self.people.append(andreas)

    def add_employee(self, form):
        """ Add a new employee from form, add_employee.html """
        empl = Employee(
            form["firstname"],
            form["lastname"],
            form["salary"],
            form["hired"]
        )
        self.people.append(empl)

    def save_data(self):
        """ Serializes each object and puts them into a list. """
        data = {}
        data["Employees"] = [e.to_json() for e in self.people]
        # Samma kod fast utan list comprehension
        # people = []
        # for e in self.people:
        #    people.append(e.to_json()
        # data["Employees"] = people

        with open(Handler.filename, 'w', encoding="utf8") as fh:
            json.dump(data, fh, indent=4)

    def load_data(self):
        """ Reads the file with filename and deserializes the data. """
        with open(Handler.filename, 'r', encoding="utf8") as fh:
            data = json.load(fh)

        if data:
            self.people = [Employee.from_json(e) for e in data["Employees"]]
        # Samma kod fast utan list comprehension
        # self.people = []
        # for e in data["Employees"]:
        #    self.people.append(Employee.from_json(e))
