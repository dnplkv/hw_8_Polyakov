import json
import datetime


class Persons():
    """Person object
    """

    def __init__(self, file_path):
        """Person properties
        """

        configs = open(file_path)
        config = json.loads(configs.read())

        self.name = config['name']
        self.surname = config['surname']
        self.birth_year = config['birth_year']
        self.sex = None

    def get_age(self):
        """Method for getting age by provided birth year"""
        now = datetime.datetime.now()
        current_year = now.year
        age = current_year - self.birth_year
        return age

    def set_sex(self, sex):
        """Method for adding sex of a person"""
        self.sex = sex
        return sex


class Students(Persons):

    pass


class Tutors(Persons):

    pass

student_1 = Persons(file_path='persons_config.json')
print(student_1.get_age())
print(student_1.set_sex(sex='Male'))
print(student_1.sex)
