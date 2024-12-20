import pprint

students = {

    1: {
        'id': '10001',
        'name': 'Spongebob',
        'age': 30,
        'gpa': 3.2,
        'fulltime': False
    },
    2: {
        'id': '10002',
        'name': 'Patrick',
        'age': 38,
        'gpa': 1.5,
        'fulltime': False
    },
    3: {
        'id': '10003',
        'name': 'Gary',
        'age': None,
        'gpa': 2.5,
        'fulltime': True
    },
    4: {
        'id': '10004',
        'name': 'Larry',
        'age': 32,
        'gpa': 2.8,
        'fulltime': False,
        'registered_date': '2024-12-05',
        'graduation_date': None,
        'courses': ['Biology', 'Chemistry', 'Calculus'],
        'address': {
            'street': '123 Fake street',
            'city': 'Bikini Bottom',
            'zipcode': 12345
        }
    },
}

print()
# print(students[4]['courses'][1])
# pprint.pp(students, indent=2, width=70, depth=3)

for student in students.keys():
    if students[student]['name'] == 'Larry':
        print(f"My name is {students[student]['name']} and my address is {students[student]['address']['street']}, {
              students[student]['address']['city']}, {students[student]['address']['zipcode']}")
    else:
        print(f"My name is {students[student]
              ['name']}, my address is unavailable")


pupils = [

    {
        'id': '10001',
        'name': 'Spongebob',
        'age': 30,
        'gpa': 3.2,
        'fulltime': False
    },
    {
        'id': '10002',
        'name': 'Patrick',
        'age': 38,
        'gpa': 1.5,
        'fulltime': False
    },
    {
        'id': '10003',
        'name': 'Gary',
        'age': None,
        'gpa': 2.5,
        'fulltime': True
    },
    {
        'id': '10004',
        'name': 'Larry',
        'age': 32,
        'gpa': 2.8,
        'fulltime': False,
        'registered_date': '2024-12-05',
        'graduation_date': None,
        'courses': ['Biology', 'Chemistry', 'Calculus'],
        'address': {
            'street': '123 Fake street',
            'city': 'Bikini Bottom',
            'zipcode': 12345
        }
    }
]
