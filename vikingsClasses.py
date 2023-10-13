
# Soldier


class Soldier:
    def __init__(self, health, strength): 
        self.health = health
        self.strength = strength
    
    def attack(self): 
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        

        
    


# Viking


class Viking (Soldier):
    
    def __init__ (self, name, health, strength):
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



class Saxon (Soldier):
    
    def __init__ (self, health, strength):
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
            return f"A Saxon has died in combat"


# War

class War(Saxon, Viking):

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

        
    def addViking(self, Viking): 
        self.vikingArmy.append(Viking)

        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon) 

        
    def vikingAttack(self):
        import random
        chosen_viking = random.choice(self.vikingArmy)
        chosen_saxon = random.choice(self.saxonArmy)
        viking_attack = chosen_saxon.receiveDamage(chosen_viking.attack())
        if chosen_saxon.health < 1:
            self.saxonArmy.remove(chosen_saxon)
        return viking_attack

        

    def saxonAttack(self): 
        import random
        chosen_viking = random.choice(self.vikingArmy)
        chosen_saxon = random.choice(self.saxonArmy)
        viking_attack = chosen_viking.receiveDamage(chosen_saxon.attack())
        if chosen_viking.health < 1:
            self.vikingArmy.remove(chosen_viking)
        return viking_attack


    def showStatus(self): 

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0: 
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."
            