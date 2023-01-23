''' Comment '''

class Person():
    ''' Comment '''

    def __init__(self, firstname, lastname):
        ''' Comment '''
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        ''' Comment '''
        return self.first + ' ' + self.last

p = Person("Andreas", "Arnesson")

p.last = "Awesome"

print(p.fullname)
