person1 = {
    'first_name': 'Petya',
    'last_name': 'Petrov',
    'age': 17,
    'role': 'student',
    'person_additional_data': {
        'average_mark': 5
    }
}

person2 = {
    'first_name': 'Vasia',
    'last_name': 'Pupkin',
    'age': 44,
    'role': 'teacher',
    'person_additional_data': {
        'experience_month': 60,
        'salary': {
            'amount': 800,
            'currency': 'UAH'
        }
    }
}


class School:
    def __init__(self, name):
        self.name = name
        self.persons = []

    def add_person(self, persons_info):

        role = persons_info['role']

        if role == 'teacher':
            self.persons.append(Teacher(persons_info))

        elif role == 'head_teacher':
            self.persons.append(HeadTeacher(persons_info))

        elif role == 'director':
            self.persons.append(Director(persons_info))

        elif role == 'student':
            self.persons.append(Student(persons_info))

        elif role == 'monitor':
            self.persons.append(Monitor(persons_info))


class Person:
    def __init__(self, persons_info):
        self.first_name = persons_info['first_name']
        self.last_name = persons_info['last_name']
        self.age = persons_info['age']


class Teacher(Person):
    def __init__(self, persons_info):
        Person.__init__(self, persons_info)
        self.experience_month = persons_info['person_additional_data'][
            'experience_month']
        self.salary = persons_info['person_additional_data']['salary']


class HeadTeacher(Teacher):
    pass


class Director(Teacher):
    pass


class Student(Person):
    def __init__(self, persons_info):
        Person.__init__(self, persons_info)
        self.average_mark = persons_info['person_additional_data'][
            'average_mark']


class Monitor(Student):
    pass


s81 = School('School #81')

s81.add_person(person1)
s81.add_person(person2)

for p in s81.persons:
    print(vars(p))
