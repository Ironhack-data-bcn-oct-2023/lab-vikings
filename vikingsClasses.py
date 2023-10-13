
# Soldier


class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage (self, damage):
        self.health = self.health - damage




# Viking



class Viking (Soldier):
    
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        
    def receiveDamage(self, damage):
        self.health = self.health - damage

        if self.health > damage:
            return f"{self.name} has received {damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin owns you all!".title()

        


# Saxon


class Saxon (Soldier):

    def __init__ (self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self,damage):
        self.health = self.health - damage

        if self.health > damage:
            return f"A Saxon has received {damage} points of damage"
        else: 
            return f"A Saxon has died in combat"



# War
import random as rm

class War:
    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking:Viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon:Saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        
        random_index = rm.randint(0, len(self.saxonArmy) - 1)
        random_saxon: Saxon = self.saxonArmy[random_index]
        self.saxonArmy.pop(random_index)

        random_viking: Viking = rm.choice(self.vikingArmy)

        result_calling = random_saxon.receiveDamage(random_viking.strength)
        
        if random_saxon.health > 0:
            self.saxonArmy.append(random_saxon)

        return result_calling
    
    def saxonAttack(self):

        random_index = rm.randint(0, len(self.vikingArmy) -1)
        random_viking: Viking = self.vikingArmy[random_index]
        self.vikingArmy.pop(random_index)

        random_saxon: Saxon = rm.choice(self.saxonArmy)

        result_calling = random_viking.receiveDamage(random_saxon.strength)
        
        if random_viking.health > 0:
            self.vikingArmy.append(random_viking)

        return result_calling
    
    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



