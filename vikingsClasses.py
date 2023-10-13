
# Soldier

import random as rd 

class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self. strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

            

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

    
# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
    

# War


class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking_obj):
        self.vikingArmy.append(Viking_obj)

    def addSaxon(self, Saxon_obj):
        self.saxonArmy.append(Saxon_obj)

    def vikingAttack(self):
        Saxon_rand = self.saxonArmy[rd.randint(0,len(self.saxonArmy)-1)]
        Viking_rand = self.vikingArmy[rd.randint(0, len(self.vikingArmy)-1)]

        
        if Saxon_rand.health <= Viking_rand.attack():
            self.saxonArmy.remove(Saxon_rand)
            
        return Saxon_rand.receiveDamage(Viking_rand.attack())  

    def saxonAttack(self):
        Saxon_rand = self.saxonArmy[rd.randint(0,len(self.saxonArmy)-1)]
        Viking_rand = self.vikingArmy[rd.randint(0, len(self.vikingArmy)-1)]

        if Viking_rand.health <= Saxon_rand.attack():
            self.vikingArmy.remove(Viking_rand)
        
        return Viking_rand.receiveDamage(Saxon_rand.attack())


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."    

