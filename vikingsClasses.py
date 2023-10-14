
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


class War():
    def __init__(self):
    
        self.vikingArmy = []
        self.saxonArmy = []
    

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        a= Saxon.receiveDamage(Viking.attack(self))
        self.saxonArmy=[i for i in self.saxonArmy if Saxon.health > 0]
        return a , Viking.attack(self)
    

    def saxonAttack(self):
        b = Viking.receiveDamage(Saxon.attack(self))
        self.vikingArmy=[i for i in self.vikingArmy if Viking.health > 0]
        return b , Saxon.attack(self)
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len (self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

