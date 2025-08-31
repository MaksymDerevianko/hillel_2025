def process_people(people_records, new_record):
    # Додаємо новий запис на початок
    modified = [new_record] + people_records

    # Міняємо місцями 1 і 5 елементи
    modified[1], modified[5] = modified[5], modified[1]

    # Беремо вік людей з індексів 6, 10, 13
    indices = [6, 10, 13]
    ages = []
    for idx in indices:
        if idx < len(modified):
            ages.append(modified[idx][2])

    all_ok = all(age >= 30 for age in ages)
    return modified, ages, all_ok


# Перевірка, якщо запускати напряму
if __name__ == "__main__":
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

    for i, rec in enumerate(modified):
        print(f"{i}: {rec}")
    print(f"Ages: {ages}")
    print(f"All ages >= 30? {all_ok}")
