
import random

# Soldier
class Soldier():
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage


# Viking
class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
         self.health -= damage
         if self.health>0:
             return f"{self.name} has received {damage} points of damage"
         else:
             return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
        
        
# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# War
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon) 
    
    def vikingAttack(self):
        saxon_herido = random.choice(self.saxonArmy)
        vikingo_ataca = random.choice(self.vikingArmy)
        string = saxon_herido.receiveDamage(vikingo_ataca.strength)            
        if saxon_herido.health <= 0:
            self.saxonArmy.remove(saxon_herido)
        return string
        
    def saxonAttack(self):
        vikingo_herido = random.choice(self.vikingArmy)
        saxon_ataca = random.choice(self.saxonArmy)
        string = vikingo_herido.receiveDamage(saxon_ataca.strength)
        if vikingo_herido.health <= 0:
            self.vikingArmy.remove(vikingo_herido)
        return string
    
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."