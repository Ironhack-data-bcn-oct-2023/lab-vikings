
# Soldier


class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack (self):
        return self.strength
    
    def receiveDamage(self, damage):

        self.health = self.health - damage


# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        

    def attack(self):
        return super().attack()
    
    def receiveDamage(self, damage):

        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

    

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    

# War

import random

class War(Viking, Saxon):

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking: Viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon: Saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        Saxon_selected = random.randint(0,len(self.saxonArmy)-1)
        saxon: Saxon = self.saxonArmy[Saxon_selected]
        
        viking_selected = random.randint(0, len(self.vikingArmy)-1)
        viking: Viking = self.vikingArmy[viking_selected]
        
        result = saxon.receiveDamage(viking.strength)

        
        if saxon.health < 1:
            self.saxonArmy.remove(saxon)

        return result
        

    def saxonAttack(self):

        Saxon_selected = random.randint(0,len(self.saxonArmy)-1)
        saxon: Saxon = self.saxonArmy[Saxon_selected]
        
        Viking_selected = random.randint(0, len(self.vikingArmy)-1)
        viking: Viking = self.vikingArmy[Viking_selected]

        result = viking.receiveDamage(saxon.strength)

        if viking.health < 1:
            self.vikingArmy.remove(viking)

        return result

       
    
    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."





