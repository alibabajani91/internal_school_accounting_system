import os

print("wellcome to s-a.")
print("developed by alibabajani.")

def add_student():
    name = input("name:")
    student_code = input("student code:")
    funds = input("funds:")
    if os.path.exists(name) == False:
        os.mkdir(f"{name}")
        n = open(f"{name}/name.txt", "w+")
        n.write(name)
        s = open(f"{name}/student_code.txt", "w+")
        s.write(student_code)
        f = open(f"{name}/funds.txt", "w+")
        f.write(funds)
        print("student sucssesfuly added.")
    else :
        print("this student have a acount")
def load_student():
    name = input("name:")
    if os.path.exists(name):
        n = open(f"{name}/name.txt", "r")
        print(f"name:{n.read()}")
        s = open(f"{name}/student_code.txt", "r")
        print(f"student code:{s.read()}")
        f = open(f"{name}/funds.txt", "r")
        print(f"funds:{f.read()}")
    else :
        print("there is not ant student with this name")