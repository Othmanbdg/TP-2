#Devoir Mr Gorce


import mysql.connector
import random

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="videotheque")

cursor = conn.cursor()
request= 'select * from user'
cursor.execute(request)
users=cursor.fetchall()

request2='select * from film '
cursor.execute(request2)
films=cursor.fetchall()

request3='select * from acteur '
cursor.execute(request3)
acteurs=cursor.fetchall()

request4='select * from jouer '
cursor.execute(request4)
jouer=cursor.fetchall()

request5='select * from realisateur '
cursor.execute(request5)
realisateurs=cursor.fetchall()
def Affiche():
    name=input("Quel est votre prénom?\n")
    print()
    nom=input("Quel est votre nom ?\n")

    couple=(nom,name)
    for ui in users:
        if ui == couple:
            print("Bonjour, "+couple[0]+" "+couple[1])







def Add_user():
    mail=input('Quel est votre email?\n')
    print()
    name=input("Quel est votre prénom?\n")
    print()
    nom=input("Quel est votre nom ?\n")
    print()
    mdp=input("Saisissez votre mot de passe")
    req="INSERT INTO user (nom,prenom,mail,mdp) VALUES (%s,%s,%s,%s)"
    attr=(nom,name,mail,mdp)
    cursor.execute(req,attr)
    conn.commit()


def recherche():
    f=input("Saisissez un films\n")
    for ui in title:
        for iu in ui:
            if f in iu:print(iu)

def recherche_real():
    f=input("Saisissez un films\n")
    for ui in films:
        if f in ui[1]:
            for iu in realisateurs:
                if iu[0]==ui[-1]:
                    print(ui[1]+" est réalisé par "+iu[1]+" "+iu[2])


def recherche_acteur():
    f=input("Saisissez un films\n")
    for ui in films:
        act=[]
        if f in ui[1]:
            for iu in realisateurs:
                if iu[0]==ui[-1]:
                    for bn in jouer:
                        if bn[0]==ui[0]:
                            for cv in acteurs:
                                if bn[1]==cv[0]:
                                    if ui[1] not in act:
                                        act.append(ui[1])
                                    if iu[1] not in act:
                                        act.append("est réaliser par ")
                                        act.append(iu[1])
                                    if iu[2] not in act:
                                        act.append(iu[2])
                                        act.append(". Les acteurs sont :\n")
                                    act.append(cv[1])
                                    act.append(cv[2])
                                    act.append(",")
            print(" ".join(act))
            print()

def Rd():
    LL=[Affiche,Add_user,recherche,recherche_real,recherche_acteur]
    ui=random.choice(LL)
    ui()