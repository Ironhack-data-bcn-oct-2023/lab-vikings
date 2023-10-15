import random as rd
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage   
        


# Viking
class Viking(Soldier):

    def __init__(self, name, health, strength):
        Soldier.__init__(self, health, strength)
        self.name = name
    

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {str(damage)} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry (self):
        return f"Odin Owns You All!"
    


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        Soldier.__init__(self, health, strength)


    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vik):
        self.vikingArmy.append(vik)


    def addSaxon(self, sax):
            self.saxonArmy.append(sax)

    def vikingAttack(self):
        vik = rd.choice(self.vikingArmy)
        sax = rd.choice(self.saxonArmy)
        damage_sax = sax.receiveDamage(vik.attack())

        if sax.health <= 0:
            self.saxonArmy.remove(sax)

        return damage_sax

    def saxonAttack(self):
        vik = rd.choice(self.vikingArmy)
        sax = rd.choice(self.saxonArmy)

        damage_viking = vik.receiveDamage(sax.attack()) 

        if vik.health <= 0 :
            self.vikingArmy.remove(vik)

        return damage_viking

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        


        