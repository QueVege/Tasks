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

person3 = {
    'first_name': 'Jelly',
    'last_name': 'Fish',
    'age': 34,
    'role': 'teacher',
    'person_additional_data': {
        'experience_month': 60,
        'salary': {
            'amount': 800,
            'currency': 'UAH'
        }
    }
}


class Person:
    def __init__(self, person_info):
        self.first_name = person_info.get('first_name')
        self.last_name = person_info.get('last_name')
        self.age = person_info.get('age')

        if not all([
            self.first_name,
            self.last_name,
            self.age]):

            raise RuntimeError(
                "Invalid person's info: "
                "should contains "
                "first_name, last_name and age.")

        if 'person_additional_data' not in person_info:
            raise RuntimeError(
                "Invalid person's info: "
                "should contains person_additional_data")
            

class Teacher(Person):
    def __init__(self, person_info):
        Person.__init__(self, person_info)

        self.experience_month = person_info[
            'person_additional_data'].get(
            'experience_month')

        self.salary = person_info[
            'person_additional_data'].get(
            'salary')

        if not all([
            self.experience_month,
            self.salary]):

            raise RuntimeError(
                "Invalid person's info: person_additional_data "
                f"for {person_info['role']} should contains "
                "experience_month and salary.")


class HeadTeacher(Teacher):
    pass


class Director(Teacher):
    pass


class Student(Person):
    def __init__(self, person_info):
        Person.__init__(self, person_info)

        self.average_mark = person_info[
            'person_additional_data'].get(
            'average_mark')

        if not self.average_mark:
            raise RuntimeError(
                "Invalid person's info: person_additional_data "
                f"for {person_info['role']} should contains "
                "average_mark.")


class Monitor(Student):
    pass


class School:
    roles = {
        'teacher': Teacher,
        'head_teacher': HeadTeacher,
        'director': Director,
        'student': Student,
        'monitor': Monitor
    }

    def __init__(self, name):
        self.name = name
        self.persons = []

    def add_person_by_role(self, person_info):
        role = person_info.get('role')

        if role in self.roles:
            self.persons.append(self.roles[role](person_info))
        else:
            raise RuntimeError(f"Invalid person's info: unindefined role")

    def add_persons(self, *adding_persons):
        for p in adding_persons:
            self.add_person_by_role(p)

    def show_persons(self):
        for p in self.persons:
            print(vars(p))


if __name__ == '__main__':

    s81 = School('School #81')
    s81.add_persons(person1, person2, person3)
    s81.show_persons()
