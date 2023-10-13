import random

# Soldier
class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    
    def __init__(self, name, health, strenght):
        super().__init__(health, strenght)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    
    def __init__(self, health, strenght):
        super().__init__(health, strenght)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
class War(Viking, Saxon):
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking: Viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon: Saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        random_idx = random.randint(0, len(self.saxonArmy) - 1)
        random_sax: Saxon = self.saxonArmy[random_idx]
        self.saxonArmy.pop(random_idx)
        random_vik: Viking = random.choice(self.vikingArmy)
        res = random_sax.receiveDamage(random_vik.strength)
        if random_sax.health > 0:
            self.saxonArmy.append(random_sax)
        return res
    
    def saxonAttack(self):
        random_idx = random.randint(0, len(self.vikingArmy) - 1)
        random_vik: Viking = self.vikingArmy[random_idx]
        self.vikingArmy.pop(random_idx)
        random_sax: Saxon = random.choice(self.saxonArmy)
        res = random_vik.receiveDamage(random_sax.strength)
        if random_vik.health > 0:
            self.vikingArmy.append(random_vik)
        return res
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if (len(self.saxonArmy) & len(self.vikingArmy)) == 1:
            return "Vikings and Saxons are still in the thick of battle."




