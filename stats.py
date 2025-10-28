import json
from collections import defaultdict

with open('staff.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


def total_salary(dept_name, data):
    total = 0
    for emp_id, emp_data in data.items():
        if emp_data['dept'] == dept_name:
            total += emp_data['salary']
    return total


print(total_salary('r&d', data))


def coun_nguyen_lastname(data):
    count = 0
    for emp_id, emp_data in data.items():
        name = emp_data['name']
        lastname = name.split()[0].lower()
        if lastname == 'nguyen':
            count += 1
    return count


print(coun_nguyen_lastname(data))

def count_user_gmail(data):
    count_user = 0
    for emp_id, emp_data in data.items():
        if '@gmail.com' in emp_data['email'] :
            count_user += 1
    return count_user
print(count_user_gmail(data))

