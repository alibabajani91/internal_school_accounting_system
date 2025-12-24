import time
import os

print("wellcome to school-acounting.")
print("developed by alibabajani.")

def add_student():
    name = input("name:")
    if os.path.exists(f"acounts/{name}") == False:
        student_code = input("student code:")
        funds = input("funds:")
        os.mkdir(f"accounts/{name}")
        n = open(f"accounts/{name}/name.txt", "w+")
        n.write(name)
        s = open(f"accounts/{name}/student_code.txt", "w+")
        s.write(student_code)
        f = open(f"accounts/{name}/funds.txt", "w+")
        f.write(funds)
        print("student sucssesfuly added.")
    else :
        print("this student have a acount")
def load_student():
    name = input("name:")
    if os.path.exists(f"acounts/{name}"):
        n = open(f"accounts/{name}/name.txt", "r")
        print(f"name:{n.read()}")
        s = open(f"accounts/{name}/student_code.txt", "r")
        print(f"student code:{s.read()}")
        f = open(f"accounts/{name}/funds.txt", "r")
        print(f"funds:{f.read()}")
    else :
        print("there is not ant student with this name")
def buy():
    name = input("name:")
    if os.path.exists(f"acounts/{name}"):
        Purchase_amount = int(input("Purchase amount:"))
        fr = open(f"accounts/{name}/funds.txt", "r")
        funds = fr.read()
        funds = int(funds) - int(Purchase_amount)
        fw = open(f"accounts/{name}/funds.txt", "w")
        fw.write(str(funds))
        loging(name,Purchase_amount)
        print("sucssesfuly")
    else :
        print("there is not ant student with this name")
def add_funds():
    name = input("name:")
    if os.path.exists(f"acounts/{name}"):
        amount = int(input("amount:"))
        fr = open(f"accounts/{name}/funds.txt", "r")
        funds = fr.read()
        funds = int(funds) + int(amount)
        fw = open(f"accounts/{name}/funds.txt", "w")
        fw.write(str(funds))
        print("sucssesfuly")
    else :
        print("there is not ant student with this name")
def re_funds():
    name = input("name:")
    if os.path.exists(f"acounts/{name}"):
        re_fund_amount = int(input("re funds amount:"))
        fr = open(f"accounts/{name}/funds.txt", "r")
        funds = fr.read()
        funds = int(funds) - int(re_fund_amount)
        fw = open(f"accounts/{name}/funds.txt", "w")
        fw.write(str(funds))
        print("sucssesfuly")
    else :
        print("there is not ant student with this name")
def loging(name,Purchase_amount):
    f = open("log.txt", "a")
    f.write(f"the {name} in {time.ctime(time.time())} Purchased {Purchase_amount}.\n")
    f.close()
while True:
    cmd = input(">:")
    if cmd == "add student":
        add_student()
    elif cmd == "load student":
        load_student()
    elif cmd == "buy":
        buy()
    elif cmd == "add fund":
        add_funds()
    elif cmd == "refunds":
        re_funds()
    elif cmd == "":
        pass
    else:
        print("there isn't any command with this name")