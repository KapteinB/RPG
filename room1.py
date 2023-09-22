php = 100
import random
ehp = 100
mercy = 0
input("they dont look friendly!")

def rom1():
    global php
    if php >= 100:
        php = 100
    if php <= 0:
        print()
        print("||   ||    ||||||     ||    ||")
        print(" || ||    ||    ||    ||    ||")
        print("  |||     ||    ||    ||    ||")
        print("  |||      ||||||      ||||||")
        print()
        print("|||||     |||    ||  ||      ||||||  |||| ")
        print("||       || ||   ||  ||      ||      ||  ||")   
        print("|||||   |||||||  ||  ||      ||||    ||  ||")
        print("||      ||   ||  ||  ||      ||      ||  ||") 
        print("||      ||   ||  ||  ||||||  ||||||  |||| ")
        print()
        exit()
    print(".")
    print("The enemy stands in your way")
    print("hp:", php)
    print("enemy hp:", ehp)
    print("mercy", mercy * 5, "%")
    valg = input("What will you do? A: Attack B: Heal C: Talk D: block --> ")
    print(".")
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
        print("you ate the best gormet food you ever tasted +50 hp")
        php = php + 50
        rom2()
    if rng == 6:
        print("you ate taco.")
        print("you got severe diarrhea")
        rom2()

def talk():
    global mercy
    global php
    if mercy > 19:
        global routing
        print("you established communism")
        print("peace was restored")
        print("you gain 0 exp")
        print("you gained 1 comrade")
        routing = 2
        proseed()
    rng = input("what will you mention? A: Memes B: history C: spell D: Poletics --> ")
    rng2 = random.randint(1,2)
    if rng == "A":
        print("You discuss how you shal rule the meme econemy")
        mercy = mercy + 1
        rom2()
    if rng == "A" and rng2 == 2:
        print("you talk about the latest events that are relevant in meme culture")
        mercy = mercy + 2
    if rng == "B":
        print("you have a discussion on world history")
        print("they dont really care")
        rom2()
    if rng == "C" and rng2 == 1:
        print("you got the enemy test a new spell on you. it was a healing spell")
        php = php + 15
        mercy = mercy + 1
        rom2()
    if rng == "C" and rng2 == 2:
        print("you got the enemy test a new spell on you. it was a fire spell")
        php = php - 15
        mercy = mercy + random.randint(1,2)
        rom2()
    if rng == "D":
        print("you figure out that taiwan isnt real")
        print("you gain 20 social credit (it has no importance)")
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
        global routing
        routing = 1
        print("the enemy had been defeated")
        print("you gained", php, "exp")
        print("you gain 0 friends")
        proseed()
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
        print("the enemy pulls up a glock and shoots you in your skull giving you Major Brain Damage.")
        php = php - 25
        rom1()
    if rng == 6:
        print("the enemy uses nuclear artillery")
        php = php - 50
        rom1()

def rom3():
    global php
    if php >= 100:
        php = 100
    if php <= 0:
        print()
        print("||   ||    ||||||     ||    ||")
        print(" || ||    ||    ||    ||    ||")
        print("  |||     ||    ||    ||    ||")
        print("  |||      ||||||      ||||||")
        print()
        print("|||||     |||    ||  ||      ||||||  |||| ")
        print("||       || ||   ||  ||      ||      ||  ||")   
        print("|||||   |||||||  ||  ||      ||||    ||  ||")
        print("||      ||   ||  ||  ||      ||      ||  ||") 
        print("||      ||   ||  ||  ||||||  ||||||  |||| ")
        print()
        exit()
    print(".")
    print("The enemy leader stands in your way")
    print("hp:", php)
    print("enemy hp:", ehp)
    print("mercy", mercy * 5, "%")
    valg = input("What will you do? A: Attack B: Heal C: Talk D: block --> ")
    print(".")
    
    if valg == "A":
        attac2()

    if valg == "B":
        heal2()
    
    if valg == "C":
        talk2()

    if valg == "D":
        defence2()

def attac2():
    global php 
    global ehp
    rng = random.randint(1,5)
    if rng == 1:
        print("you violently stab the enemy 20 dmg (using a gun)")
        print("a knife would have done more damage tbh")
        ehp = ehp - 20
        rom4()
    if rng == 2:
        print("you punch the enemy 15 dmg")
        ehp = ehp - 15
        rom4()
    if rng == 3:
        print("you slap the enemy 10 dmg")
        ehp = ehp - 10
        rom4()
    if rng == 4:
        print("you try to hit the enemy. they felt bad for you and lowered their healh bar 5 dmg")
        ehp = ehp - 5
        rom4()
    if rng == 5:
        print("you try to punch but give up right before you trip")
        rom4()
    if rng == 6:
        print("you gave the enemy a taco")
        print("they got diarrhea but that doenst do anything here")
        rom3()


def heal2():
    global php
    rng = random.randint(1,6)
    if rng == 1:
        print("you consumed a lot of health items +35 hp")
        php = php + 35
        rom4()
    if rng == 2:
        print("you eat B U R G E R +30 hp")
        php = php + 30
        rom4()
    if rng == 3:
        print("you gained hp. idk how but you did. +25 hp")
        php = php + 25
        rom4()
    if rng == 4:
        print("you concidered using healing items but didnt. but its the thought that counts +20 hp")
        php = php +20
        rom4()
    if rng == 5:
        print("you ate the best gormet food you ever tasted +50 hp")
        php = php + 50
        rom4()
    if rng == 6:
        print("you ate taco.")
        print("you got severe diarrhea")
        rom4()

def talk2():
    global mercy
    global php
    rng = input("what will be discussed? A: Memes B: history C: make fun of something D: spell E: politics --> ")
    rng2 = random.randint(1,4)
    rng3 = random.randint(1,2)
    if mercy >= 20:
        print("you established communism")
        print("peace was finally restored")
        print("you gain 0 exp")
        print("you gained 1 comrade")
        print()
        print("You Win")
        if routing == 2:
            print("Ending 8: Mercyfull ending")
            print("taling solves most problems")
        if routing == 1:
            print("Ending 9: Big Brain Time. ending")
            print("why did u decide to spare the leader")
            print("and not the goon (or he died to recoil damage but idc)")
        exit()
    if rng == "A":
        print("You discuss how you shal rule the meme econemy")
        print("they were too old to onderstand what any of your words ment")
        rom4()
    if rng == "B":
        print("you have an hour long discussion on world history")
        mercy = mercy + 2
        rom4()
    if rng == "C" and rng2 == 1:
        print("you make fun of Ohio")
        mercy = mercy + 1
        rom4()
    if rng == "C" and rng2 == 2:
        print("you make fun of Florida")
        mercy = mercy + 1
        rom4()
    if rng == "C" and rng2 == 3:
        print("you make fun of Texas")
        mercy = mercy + 1
        rom4()
    if rng == "C" and rng2 == 4:
        print("you make fun of the local homeless population")
        mercy = mercy + 1
        rom4()
    if rng == "D" and rng3 == 1:
        print("you got the enemy test a new spell on you. it was a healing spell")
        php = php + 15
        mercy = mercy + 1
        rom4()
    if rng == "D" and rng3 == 2:
        print("you got the enemy test a new spell on you. it was a fire spell")
        php = php - 15
        mercy = mercy + 1
        rom4()
    if rng == "E":
        print("you figure out that taiwan isnt real")
        print("you gain 30 social credit (it has no importance)")
        rom4()


def defence2():
    global php
    global ehp
    print("you realise this command isnt conna help you")
    rom3()


def rom4():
    global php
    global ehp
    if ehp <= 0:
        print("the enemy had been defeated")
        print("you gained", php, "exp")
        print("you gain 0 friends")
        print()
        print("You Win")
        if routing == 1:
            print("Ending 2: Fighter in a new dimention")
            print("What problem cant be solved with violence?")
        if routing == 2:
            print("Ending 10: Overthrow the leaders!! Ending")
            print("all the goons can now be free from the leaders controll")
            print("what control?")
            print("idk")
        exit()
    rng = random.randint(1,6)
    if rng == 1:
        print("the enemy slapped you in your face")
        php = php - 10
        rom3()
    if rng == 2:
        print("the enemy kicks your foot making you loose balance and you land on them")
        php = php - 15
        ehp = ehp - 5
        rom3()
    if rng == 3:
        print("the enemy pulls up a phone and uses social media to deal damage")
        php = php - 10
        rom3()
    if rng == 4:
        print("the enemy forgor that it also gets turns")
        rom3()
    if rng == 5:
        print("the enemy steals your liver but that has no importance in this game in any way")
        print("he did get a lot of money from it though")
        print("you get none of it")
        rom3()
    if rng == 6:
        print("the enemy pulls up a glock and shoots you in your skull giving you Major Brain Damage. But there were no more brain damage to get")
        php = php - 25
        rom3()
    if rng == 6:
        print("the enemy uses nuclear artillery")
        php = php - 50
        rom3()

def proseed():
    global ehp
    global mercy
    print("you move on")
    print("the leader of the enemy sees you")
    input("guess theres another battle huh")
    ehp = 150
    mercy = 0
    rom3()
rom1()