basic = int(input("Enter The Basic Salaray: "))
hra = 0.2*basic
da = 0.5*basic
pf = 0.11*basic
grade = input("Enter the grade: ")
match grade:
    case 'A':
        allow = 1700
    case 'B':
        allow = 1700
    case _:
        allow = 1300
total_salary = basic + hra + da - pf +allow
print(f"Total Salaray{total_salary}")