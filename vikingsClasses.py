
import random
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
            
        
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage 
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage 
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return "A Saxon has died in combat"
        


# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
          
    def vikingAttack(self): 
        randomsaxons = random.choice(self.saxonArmy)
        randomviking = random.choice(self.vikingArmy)
        
        damage_saxon = randomsaxons.receiveDamage(randomviking.strength)
        if randomsaxons.health <= 0:
            self.saxonArmy.remove(randomsaxons)
        return damage_saxon
    
    def saxonAttack(self): 
        randomsaxons = random.choice(self.saxonArmy)
        randomviking = random.choice(self.vikingArmy)
        
        damage_viking = randomviking.receiveDamage(randomsaxons.strength)
        if randomviking.health <= 0:
            self.vikingArmy.remove(randomviking)
        return damage_viking
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."