#!/usr/bin/env python3
"""
Handler file
"""

from employee import Employee

class Handler():
    """
    Class that handles employees
    """
    def __init__(self):
        """ Constructor """
        self.people = []
        self.add_predefined_employees()

    def get_people(self):
        """ Returns people, a list with employees """
        return self.people

    def get_list_of_names(self):
        """ Returns a list with employees' ids """
        return [(e.firstname + " " + e.lastname) for e in self.people]
        # Samma kod fast utan list comprehension
        # names = []
        # for e in self.people:
        #    names.append(e.firstname + " " + e.lastname)
        # return names

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

    def write_session(self, session):
        """ Writes to session """
        session["Employees"] = [e.to_json() for e in self.people]
        # Samma kod fast utan list comprehension
        # people = []
        # for e in self.people:
        #    people.append(e.to_json()
        # session["Employees"] = people

    def read_session(self, session):
        """ Reads from session """
        # first check if session has values, otherwise will crash if try get values
        if session.get("Employees", []):
            self.people = [Employee.from_json(e) for e in session["Employees"]]
            # Samma kod fast utan list comprehension
            # self.people = []
            # for e in session["Employees"]:
            #    self.people.append(Employee.from_json(e))
