
# Soldier


class Soldier():
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage): 
        self.health = self.health - damage
        


# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name
        self.health = health
        self.strength = strength
        

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
        

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health,strength)
        
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War

import random

class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        
        if self.saxonArmy:
            random_saxon = random.choice(self.saxonArmy)
            random_viking = random.choice(self.vikingArmy)
           
            damage = random_viking.attack()
            result = random_saxon.receiveDamage(damage)

            if random_saxon.health <= 0:
                self.saxonArmy.remove(random_saxon)
            
            return result
        return None

    def saxonAttack(self):
        
        if self.vikingArmy:
           
            random_viking = random.choice(self.vikingArmy)
            random_saxon = random.choice(self.saxonArmy)

            damage = random_saxon.attack()
            result = random_viking.receiveDamage(damage)

            if random_viking.health <= 0:
                self.vikingArmy.remove(random_viking)
            
            return result
        return None
        

        
    def showStatus(self):
        
        if len(self.saxonArmy) == 0: 
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

        

        