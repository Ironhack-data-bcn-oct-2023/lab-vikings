import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health

    def attack(self):
        return self.strength
    
    def receiveDamage(self, thedamage):
        self.thedamage = thedamage
        self.health = self.health - self.thedamage

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, thedamage):
        self.thedamage = thedamage
        self.health = self.health - self.thedamage

        if self.health > 0:
            return f"{self.name} has received {self.thedamage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, thedamage):
        self.thedamage = thedamage
        self.health = self.health - self.thedamage

        if self.health > 0:
            return f"A Saxon has received {self.thedamage} points of damage"
        else:
            return "A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        randomsaxon = random.choice(self.saxonArmy)
        randomviking = random.choice(self.vikingArmy)
        
        damage_viking = randomsaxon.receiveDamage(randomviking.strength)
        
        if randomsaxon.health <= 0:
            self.saxonArmy.remove(randomsaxon)

        return damage_viking


    def saxonAttack(self):
        randomsaxon = random.choice(self.saxonArmy)
        randomviking = random.choice(self.vikingArmy)
        
        damage_saxon = randomviking.receiveDamage(randomsaxon.strength)

        if randomviking.health <= 0:
            self.vikingArmy.remove(randomviking)

        return damage_saxon
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

        


