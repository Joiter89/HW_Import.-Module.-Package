from application.salary import calculate_salary
from application.application.db.people import get_employees
from datetime import date


if __name__ == '__main__':
    print(f'Текущая дата: {date.today().strftime("%d-%m-%Y")}')
    calculate_salary()
    get_employees()
