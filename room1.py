php = 100
import random
ehp = 100
mercy = 0

def rom1():
    global php
    if php >= 100:
        php = 100
    if php <= 0:
        print("YOU LOST")
        print("you will get them next time")
        exit()
    print("The enemy stands in your way")
    print("hp:", php)
    print("enemy hp:", ehp)
    print("mercy", mercy * 5, "%")
    valg = input("What will you do? A: Attack B: Heal C: Talk D: block ")
    
    if valg == "A":
        attac()

    if valg == "B":
        heal()
    
    if valg == "C":
        talk()

    if valg == "D":
        defence()

def attac():
    global php 
    global ehp
    rng = random.randint(1,5)
    if rng == 1:
        print("you violently stab the enemy 20 dmg")
        ehp = ehp - 20
        rom2()
    if rng == 2:
        print("you punch the enemy 15 dmg")
        ehp = ehp - 15
        rom2()
    if rng == 3:
        print("you slap the enemy 10 dmg")
        ehp = ehp - 10
        rom2()
    if rng == 4:
        print("you try to hit the enemy. they took emosional damage 5 dmg")
        ehp = ehp - 5
        rom2()
    if rng == 5:
        print("you try to punch but trip over you took 5 dmg")
        php = php - 5
        rom2()


def heal():
    global php
    rng = random.randint(1,6)
    if rng == 1:
        print("you consumed a lot of health items +35 hp")
        php = php + 35
        rom2()
    if rng == 2:
        print("you eat B U R G E R +30 hp")
        php = php + 30
        rom2()
    if rng == 3:
        print("you gained hp. idk how but you did. +25 hp")
        php = php + 25
        rom2()
    if rng == 4:
        print("you concidered using healing items but didnt. but its the thought that counts +20 hp")
        php = php +20
        rom2()
    if rng == 5:
        print("you ate the best gormet shit you ever tasted +50 hp")
        php = php + 50
        rom2()
    if rng == 6:
        print("you ate taco bell.")
        print("you got severe diarrhea")
        rom2()

def talk():
    global mercy
    global php
    rng = random.randint(1,12)
    if mercy >= 20:
        print("you established communism")
        print("peace was restored")
        print("you gain 0 exp")
        print("you gained 1 comrade")
        exit()
    if rng == 2:
        print("the enemy is convinced his mother is concidered a planet")
        rom2()
    if rng == 3:
        print("You bolth discuss who the most powerfull game character is")
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 4:
        print("You discuss how you shal rule the meme econemy")
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 5:
        print("you have an hour long discussion on world history")
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 6:
        print("you make fun of Ohio")
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 7:
        print("you make fun of Florida")
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 8:
        print("you make fun of Texas")
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 9:
        print("you make fun of the local homeless population")
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 10:
        print("you convinced the enemy to share a healing potion with you")
        php = php + 10
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 11:
        print("you got the enemy test a new spell on you. it was a healing spell")
        php = php + 15
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 1:
        print("you got the enemy test a new spell on you. it was a fire spell")
        php = php - 15
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == 12:
        print("you figure out that taiwan isnt real")
        print("you gain 20 social credit (it has no importance)")
        mercy = mercy + random.randint(1,2)
        rom2()


def defence():
    global php
    global ehp
    print("the enemy attacks")
    rng = random.randint(1,6)
    if rng == 1:
        print("you parried the enemy attack doing 10 damage to them")
        php = ehp - 10
        rom1()
    if rng == 2:
        print("You fully block the hit")
        rom1()
    if rng == 3:
        print("you block the hit reducing its damage by a lot")
        php = php - 1
        rom1()
    if rng == 4:
        print("the enemy peirces your sheild but doesnt get the full damage")
        php = php - 5
        rom1()
    if rng == 5:
        print("The enemy pretended you didnt have a sheild")
        php = php - 10
        rom1()
    if rng == 6:
        print("the enemy seeing you try to block hits instead a very vulnureble place")
        php = php - 50
        rom1()

def rom2():
    global php
    global ehp
    if ehp <= 0:
        print("the enemy had been defeated")
        print("you gained", php, "exp")
        print("you gain 0 friends")
        exit()
    rng = random.randint(1,6)
    if rng == 1:
        print("the enemy slapped you in your face")
        php = php - 10
        rom1()
    if rng == 2:
        print("the enemy kicks your foot making you loose balance and you land on them")
        php = php - 15
        ehp = ehp - 5
        rom1()
    if rng == 3:
        print("the enemy pulls up a glock and shoots you in your foot")
        php = php - 10
        rom1()
    if rng == 4:
        print("the enemy forgor that it also gets turns")
        rom1()
    if rng == 5:
        print("the enemy steals your liver but that has no importance in this game in any way")
        rom1()
    if rng == 6:
        print("the enemy pulls up a glock and shoots you in your skull giving you Major Brain Damage. But ")
        php = php - 25
        rom1()
    if rng == 6:
        print("the enemy uses nuclear artillery")
        php = php - 50
        rom1()


rom1()