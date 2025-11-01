department = {
    'Engineering':{
        1001:{'name':'Alice','salary':75000},
        1003:{'name':'Charlie','salary':80000},
    },
    'Sales':{
        1002:{'name':'Bob', 'salary':50000},
        1005:{'name':'Eve', 'salary':55000},
    },
    'Marketing':{
        1004:{'name':'Dave', 'salary':60000},
    }
}
# cho phép người dùng thêm 1 nhân viên vào danh sách,
def add_employee():
    dept_name = input('Enter the department: ')
    if dept_name not in department:
        department[dept_name]={}
        print(f'created department {dept_name}')
    else:
        print(f'Using existing department {dept_name}')
    emp_id = int(input('Enter the employee id: '))
    emp_name = input('Enter the employee name: ')
    salary = int(input('Enter the employee salary: '))
    if emp_id in department[dept_name]:
        print(f'Employee {emp_id} already exists')
        # department[dept_name][emp_id] = {'name':emp_name, 'salary':salary}
    print(f'add employee {emp_id}: {emp_name} sucessfully in {dept_name} department')
add_employee()
# tim kiem nhan vien voi ID
def find_employee():
    emp_id = int(input('Enter the employee id: '))
    for dept_name,employees in department.items():
        if emp_id in employees:
            employee = employees[emp_id]
            print(f'Found :{employee['name']} in department'
                  f' {dept_name} with salary: {employee['salary']}')
            found = True
            break
    if not found:
            print('employee not found')
find_employee()

def list_by_salary():
    min_salary = int(input('Enter the minimum salary: '))
    for dept,employees in department.items():
        for emp_id,info in employees.items():
            if info['salary'] >= min_salary:
                print(f'Found :{info["name"]} in department {dept} with salary: {info ["salary"]}')
list_by_salary()












