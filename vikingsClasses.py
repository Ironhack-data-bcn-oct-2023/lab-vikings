
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
        if not self.saxonArmy:
            return "Saxons have no soldiers remaining."
        
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        saxon_damage = random_saxon.receiveDamage(random_viking.attack())

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return saxon_damage
    
    def saxonAttack(self):
        if not self.vikingArmy:
            return "Vikings have no soldiers remaining."
        
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        viking_damage = random_viking.receiveDamage(random_saxon.attack())

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)

        return viking_damage

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
