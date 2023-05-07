from main import *

print('Hello World!')

if __name__ == '__main__':
    print(f'Текущая дата: {date.today().strftime("%d-%m-%Y")}')
    calculate_salary()
    get_employees()