import time
def consulta():
    with open("Insira.txt","r") as f:
        r = str(",".join)
        print(f.read().replace("\n","',\n'"), end = '\n')

consulta()

time.sleep(400)
