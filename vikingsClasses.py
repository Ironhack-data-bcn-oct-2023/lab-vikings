
import random as rn


# Soldier
class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage



# Viking
class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name

    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    

    def battleCry(self):
        return "Odin Owns You All!"



# Saxon
class Saxon(Soldier):
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    


# War
class War:
    def __init__(self,):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking_soldier):
        self.vikingArmy.append(viking_soldier)

    def addSaxon(self, saxon_soldier):
        self.saxonArmy.append(saxon_soldier)

    def vikingAttack(self):
        vik_soldier = self.vikingArmy[rn.randint(0,len(self.vikingArmy)-1)]
        sax_soldier = self.saxonArmy[rn.randint(0,len(self.saxonArmy)-1)] 
        if sax_soldier.health <= vik_soldier.attack():
            self.saxonArmy.remove(sax_soldier)
        return sax_soldier.receiveDamage(vik_soldier.attack())


    def saxonAttack(self):
        vik_soldier = self.vikingArmy[rn.randint(0,len(self.vikingArmy)-1)]
        sax_soldier = self.saxonArmy[rn.randint(0,len(self.saxonArmy)-1)]
        if vik_soldier.health <= sax_soldier.attack():
            self.vikingArmy.remove(vik_soldier)
        return vik_soldier.receiveDamage(sax_soldier.attack())


    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
