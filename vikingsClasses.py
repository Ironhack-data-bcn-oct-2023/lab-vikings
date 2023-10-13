
# Soldier

import random

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

    def __init__ (self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return (f"{self.name} has received {self.damage} points of damage")

        else:
            return (f"{self.name} has died in act of combat")

        
    def battleCry(self):
        return "Odin Owns You All!"
        

# Saxon

class Saxon(Soldier):
        
    def __init__ (self, health, strength):
        super().__init__(health, strength)


    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
                return (f"A Saxon has received {self.damage} points of damage")

        else:
            return (f"A Saxon has died in combat")             

# War

class War:

    
    def __init__ (self):

        self.vikingArmy = []
        self.saxonArmy = []


    def addViking(self, Viking_object):
        self.vikingArmy += [Viking_object]
        
    def addSaxon(self, Saxon_object):
        self.saxonArmy += [Saxon_object]
    
    def vikingAttack(self):
        saxon_soldier = random.choice(self.saxonArmy)
        viking_soldier = random.choice(self.vikingArmy)
        saxon_soldier_damage = saxon_soldier.receiveDamage(viking_soldier.strength)
        if saxon_soldier.health <= 0:
            self.saxonArmy.remove(saxon_soldier)
        return saxon_soldier_damage
    
    def saxonAttack(self):
        viking_soldier2 = random.choice(self.vikingArmy)
        saxon_soldier2 = random.choice(self.saxonArmy)
        viking_soldier2_damage = viking_soldier2.receiveDamage(saxon_soldier2.strength)
        if viking_soldier2.health <= 0:
            self.vikingArmy.remove(viking_soldier2)
        return viking_soldier2_damage


    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    

