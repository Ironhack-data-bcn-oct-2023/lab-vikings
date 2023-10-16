import random

# Soldier
class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
    pass

# Viking
class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry():
        return "Odin Owns You All!"
    pass

# Saxon
class Saxon:
    def __init__ (self, health, strength):
        super().__init__(health, strength)
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
    pass

# War
class War:
# 1. OUR ARMIES
    def __init__(self, vikingarmy,saxonarmy):
            self.vikingarmy = vikingarmy
            self.saxonarmy = saxonarmy

# 2. ARMIES MODIFICATIONS
    def addViking(self,viking):
        self.vikingarmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonarmy.append(saxon)
# 3.War face
    viking_random = random.choice(self.vikingarmy)  
    saxon_random = random.choice(self.saxonarmy) 
    
    def vikingAttack(self, strength):
        receiveDamage()
            result reciveDamage(Saxon)
            
    def vikingAttack():
        
    def saxonAttack():
        
    def showStatus():
      
         



    pass

