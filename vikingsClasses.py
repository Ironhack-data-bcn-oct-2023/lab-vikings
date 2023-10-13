
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
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return f"Odin Owns You All!"



# Saxon


class Saxon(Soldier):

    def receiveDamage(self, damage):
        self.health = self.health - damage
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
                
    def addViking (self,viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        random_Saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        random_Viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        

        if random_Saxon.health <= random_Viking.attack():
            self.saxonArmy.remove(random_Saxon)
        
        return random_Saxon.receiveDamage(random_Viking.attack())
        
    def saxonAttack(self):
        random_Viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        random_Saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        

        if random_Viking.health <= random_Saxon.attack():
            self.vikingArmy.remove(random_Viking)
        
        return random_Viking.receiveDamage(random_Saxon.attack())

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        





    

