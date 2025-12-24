import os

print("wellcome to s-a.")
print("developed by alibabajani.")

def add_student():
    name = input("name:")
    student_code = input("student code:")
    funds = input("funds:")
    if os.path.exists(name) == False:
        os.mkdir(f"{name}")
        open(f"{name}/{name}.txt", "w+")
        open(f"{name}/{student_code}.txt", "w+")
        open(f"{name}/{funds}.txt", "w+")
        print("student sucssesfuly added.")
