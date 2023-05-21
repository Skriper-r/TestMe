import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')


def generated_person():
    yield Person(
        full_name=faker_ru.name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10, 80),
        salary=random.randint(1000, 10000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )
