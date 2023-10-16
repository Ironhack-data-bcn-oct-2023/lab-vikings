from vikingsClasses import War, Viking, Saxon
import random


l_names = ["Oriol","Ricardo","Javier","Aida","Pati.Z","Pere","Ana","Victor","Marc","Sara","Esther","Marta","Miki","Amir","Noe","Emma","Junior","Martina","Félix","Lucia","Edu","Marco","León","Patricia.S","Maira","Clàudia"]

def generateViking():
            v_name = v_name = random.choice(l_names)
            v_strength = random.randint(75,150)
            v_health = random.randint(100,300)
            nV =  Viking(v_name,v_health,v_strength)
            return nV
def generateSaxon():
            s_strength = random.randint(75,150)
            s_health = random.randint(100,300)
            nS =  Saxon(s_health,s_strength)
            return nS

Guerra = War()
Guerra.addSaxon(generateSaxon())
Guerra.addViking(generateViking())
Guerra.showStatus()
while Guerra.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print(Guerra.vikingAttack())
    if Guerra.showStatus() != "Vikings and Saxons are still in the thick of battle.":
        break
    print(Guerra.saxonAttack())
    if Guerra.showStatus() != "Vikings and Saxons are still in the thick of battle.":
        break
print(Guerra.showStatus())
