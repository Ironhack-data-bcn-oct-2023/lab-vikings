
# Soldier


class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack (self):
        return self.strength

    def receiveDamage (self, damage):
        self.health = self.health - damage

        

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        

    def attack (self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry (self):
        return "Odin Owns You All!"

    

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack (self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

import random

class War(Viking, Saxon):

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
      self.vikingArmy.append(Viking)
      
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
   
    def vikingAttack(self):
        random_saxon = random.randint(0, len(self.saxonArmy)-1)
        Saxon: Saxon = self.saxonArmy[random_saxon]

        random_viking = random.randint(0, len(self.vikingArmy)-1)
        Viking: Viking = self.vikingArmy[random_viking]

        saxon_damage = Saxon.receiveDamage(Viking.attack())
        if saxon_damage <= 0:
            self.saxonArmy.remove(Saxon)
        return saxon_damage
    
    def saxonAttack(self):
        random_saxon = random.randint(0, len(self.saxonArmy)-1)
        Saxon: Saxon = self.saxonArmy[random_saxon]

        random_viking = random.randint(0, len(self.vikingArmy)-1)
        Viking: Viking = self.vikingArmy[random_viking]

        viking_damage = Viking.receiveDamage(Saxon.attack())
        if viking_damage <= 0:
            self.vikingArmy.remove(Viking)
        return viking_damage

    def showStatus(self):
        for i in self.vikingArmy:
            if len(self.vikingArmy) == 0:
                return "Saxons have fought for their lives and survive another day..."
            elif len(self.saxonArmy) == 0:
                return "Vikings have won the war of the century!"
            else:
                return "Vikings and Saxons are still in the thick of battle."

