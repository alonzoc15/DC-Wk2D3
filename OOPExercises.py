class Person:
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone

    def greet(self, other_person): 
        print('Hello {}, I am {}!'.format(other_person.name, self.name))


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "Jordan@aol.com", "495-586-3456")
print(sonny.greet(jordan))
print(jordan.greet(sonny))