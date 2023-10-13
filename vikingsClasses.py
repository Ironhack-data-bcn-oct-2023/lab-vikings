
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    #attack of soldier
    def attack(self):
        return self.strength
        
    #Damage received (health -= damage)
    def receiveDamage(self, damage):
        self.health -= damage    


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
            return f"A Saxon has died in combat" 
    pass

# War

import random
class War(Saxon, Viking):
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking: Viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon: Saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        randomindex_saxon = random.randint(0, len(self.saxonArmy)-1)
        saxon: Saxon = self.saxonArmy[randomindex_saxon]
        randomindex_viking = random.randint(0,len(self.vikingArmy)-1)
        viking: Viking = self.vikingArmy[randomindex_viking]
        attack = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
           # self.saxonArmy.append(saxon)
            self.saxonArmy.pop(randomindex_saxon)

        return attack

    def saxonAttack(self):
        randomindex_viking = random.randint(0, len(self.vikingArmy)-1)
        viking: Viking = self.vikingArmy[randomindex_viking]
        
        randomindex_saxon = random.randint(0,len(self.saxonArmy)-1)
        saxon: Saxon = self.saxonArmy[randomindex_saxon]
        attack = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            #self.vikingArmy.append(viking)
            self.vikingArmy.pop(randomindex_viking)
        return attack
    
    def showStatus(self):
        if len(self.saxonArmy and self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        else:
            return "Saxons have fought for their lives and survive another day..."
        
