
# Soldier


class Soldier ():
    def __init__(self, health,strength):
        self.health = health
        self.strength = strength
    
    def attack (self):
        return self.strength
    
    def receiveDamage (self,damage):
        self.health = self.health - damage
        



# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry (self):
        return f"Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"   


# War

import random
class War():
    import random
    def __init__(self):
    
        self.vikingArmy = []
        self.saxonArmy = []
        

    def addViking(self, viking_soldier):
        self.vikingArmy.append(viking_soldier)
    
    def addSaxon(self,saxon_soldier):
        self.saxonArmy.append(saxon_soldier)
    
    def vikingAttack(self):
        saxon_soldier = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        viking_soldier = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        if saxon_soldier.health <= viking_soldier.strength:
            self.saxonArmy.remove(saxon_soldier)
           
        return saxon_soldier.receiveDamage(viking_soldier.attack())

    def saxonAttack(self):
        saxon_soldier = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        viking_soldier = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        if viking_soldier.health <= saxon_soldier.strength:
            self.vikingArmy.remove(viking_soldier)
           
        return viking_soldier.receiveDamage(saxon_soldier.attack())

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len (self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

