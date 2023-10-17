
# Soldier
#to test the soldier you do python3 name_of_file

class Soldier:
    def __init__(self, health, strength): #arguments
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        #self.damage = damage - don't need to use
        self.health = self.health - damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        #self.damage = damage
        #self.health = self.health - self.damage
        self.health = self.health - damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return (f"A Saxon has died in combat")
    

# War

class War():

    vikingArmy = []
    saxonArmy = []

    def addViking(self,Viking):
        self.vikingArmy.append(1)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(1)

    def vikingAttack(self): 
        receiveDamage = self.strength 
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")
        
    def saxonAttack():

    def showStatus():
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
    pass
