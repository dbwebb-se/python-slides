class Owner:

    def __init__(self, name, ssn, adress):
        self.name = name
        self.ssn = ssn
        self.adress = adress
        self.accounts = []

    def get_ssn(self):
        return self.ssn
