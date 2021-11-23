#Создаём функции.
from random import * 
def passcontrol(psword):
    ls=list(psword)
    for i in psword:
        if i.isdigit()== True:
            digit='True'
        if i.isalpha()== True:
            alpha='True'
        if i.isupper()==True:
            upper='True'
        if i.islower()==True:
            lower='True'
        if i in list(".,-+/%"):
            symbol='True'
    if digit=='True' and upper=='True'and alpha=='True' and lower=='True' and symbol=='True':
        ans=True
    else:
        ans=False
    return ans
def passautomat(): 
    #Пароль создаётся машиной.
    str0=". , -"
    str1="0123456789"
    str2="qwertyuiopasdfghjklzxcvbnm"
    str3=str2.upper() 
    str4=str0+str1+str2+str3
    ls=list(str4) # список, все символы выше будут в списке.
    shuffle(ls) #перемешивает значения
    # Извлекаем из списка 12 произвольных значений
    psword="".join([choice(ls) for x in range(12)])
    # Пароль готов
    return psword

def koik_kasutajad(users,passwords):
    i=0
    for user in users:
        print(users,end="-")
        print(passwords[i])
        i+=1

def register():
 users=["Nikita"]
 passwords=["12345"]
 while True:
    log=input('Kasutajatunnus')
    if log not in users:
       print('Tunnus soobib')
       break
    else:
       print('See nimi juba on olemas listis')
       break
    v=input('Arvuti-A või ise-I loob parool')
        if v.upper()=='A':
            pas=passautomat()
        elif v.upper()=='I':
            pas=input('Siseata oma parool')
            tulemus=passcontrol(pas)
            if tulemus==True:
            users.append(log)
            passwords.append(pas)
            break