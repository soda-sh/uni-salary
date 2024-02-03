import os.path as path
import formula as f

prof_list = "prof-list.txt"
prof_salary = "prof-salary.txt"

if not path.isfile(prof_list):
    print(f"{prof_list} does not exists")

if not path.isfile(prof_salary):
    print(f"{prof_salary} does not exists")

print(f"value from formula.py: {f.test}")
