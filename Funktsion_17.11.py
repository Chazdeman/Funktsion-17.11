from module1 import *
users=["Nikita"]
passwords=["12345"]

while True:
    v=int(input('Näita koike - 0\nReg-1\nAvt-2\nVälja-3\n==>'))
    if v==0:
       koik_kasutajad(users,passwords)
    elif v==1:
       register()
    elif v==2:
        print('Autoriseerimine')
        log=input('Login > ')
        if log not in users:
            print('Sina ei ole registreeritud')
        else:
            pas=input("Password > ")
            if pas not in passwords:
                print("Vale parool")
            else:
                if users.index(log)==passwords.index(pas):
                    print("Tere")