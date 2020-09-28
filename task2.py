import os
from csv import DictReader, DictWriter
from collections import defaultdict
from pprint import pprint

departments_names = set()
report = defaultdict(list)  # {name : [employees_salaryes]}

DATASET_FILENAME = 'funcs_homework_employees_sample.csv'


def read_dataset() -> None:
    """Read dataset and place data in departmenst_names
       and report variables"""

    if not os.path.exists(DATASET_FILENAME):
        print("Can't read input file. File doesnt exist: {}".format(DATASET_FILENAME))
        exit(1)

    with open(DATASET_FILENAME, 'r', encoding='utf-8') as fin:
        reader = DictReader(fin, delimiter=";")

        for row in reader:  # ФИО полностью;Должность;Отдел;Оценка;Оклад
            departments_names.add(row['Должность'])
            report[row['Отдел']].append(row['Оклад'])
    return


def print_departments() -> None:
    """Print out departmenst_names variable"""

    pprint(departments_names)


def print_report() -> None:
    """Proccess report varibale and print out"""

    for k, v in report.items():
        vv = tuple(map(int, v))
        print("Department name: {};\n"
              "Number of employees: {};\n"
              "Min salary: {};\n"
              "Max salary: {};\n"
              "Mean salary: {:.2f};\n".format(k, len(v), min(vv), max(vv), sum(vv) / len(v)))


def save_report() -> None:
    """Save report in report.csv file"""

    with open("report.csv", "w", encoding='utf-8') as fout:
        field_names = ["department_name", "employees_number",
                       "min_salary", "max_salary", "mean_salary"]
        writer = DictWriter(fout, fieldnames=field_names)
        writer.writeheader()
        for k, v in report.items():
            vv = tuple(map(int, v))
            writer.writerow({ok: ov for ok, ov in zip(
                field_names, (k, len(v), min(vv), max(vv), sum(vv) / len(v)))})


def menu() -> None:
    """Usage:
        1. Print out all departments names.
        2. Print out departments report:
            name,
            number of employees,
            min salary,
            max salary,
            mean salary.
        3. Save departments report in report.csv file.
        4. Exit."""

    actions = {
        "1": print_departments,
        "2": print_report,
        "3": save_report,
        "4": exit
    }

    options = actions.keys()

    while True:

        option = ""

        while option not in options:
            option = input("Choose action {}:\n".format(str(tuple(options))))

        assert option in actions

        actions[option]()  # call menu action


if __name__ == '__main__':
    read_dataset()
    print(menu.__doc__)
    menu()
