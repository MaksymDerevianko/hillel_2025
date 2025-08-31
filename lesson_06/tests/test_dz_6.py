import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DZ_6 import process_people


def test_process_people_logic():
    people = [
        ('John', 'Doe', 28, 'Engineer', 'New York'),
        ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
        ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
        ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
        ('Michael', 'Brown', 22, 'Student', 'Seattle'),
        ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
        ('David', 'Miller', 33, 'Software Developer', 'Austin'),
        ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
        ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
        ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
        ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
        ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
        ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
        ('Ava', 'White', 42, 'Journalist', 'San Diego'),
        ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix'),
    ]
    new = ('Maksym', 'Derevianko', 28, 'QA', 'Kyiv')

    modified, ages, all_ok = process_people(people, new)

    # перевірка індексів після додавання та обміну
    assert modified[0] == new
    assert modified[1] == people[4]  # після вставки new усі зсуваються, people[4] => modified[1]
    assert modified[5] == people[0]  # people[0] пішов на modified[5]

    # перевірка віку
    assert all(isinstance(age, int) for age in ages)
    assert isinstance(all_ok, bool)
