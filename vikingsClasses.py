
# Soldier


class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage


# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name

    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage 
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"


    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength)
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = self.health - damage
        if self.health <= 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking, Saxon):
        self.vikingArmy.append(Viking)
        self.saxonArmy.append(Saxon)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        self.viking = random.choice(self.vikingArmy)
    
    
        result = saxon.receiveDamage(viking.strength)
        if result == f"A Saxon has received {viking.strength} points of damage":
            self.saxonArmy.remove(saxon)
            return result

    def saxonAttack(self):
        self.viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
    
        result = viking.receiveDamage(saxon.strength)
        if result == f"{saxon.name} has died in act of combat":
        self.saxonArmy.remove(saxon)
        return result
    
    def showStatus(self):
        if self.saxonArmy == 0:
            return "Vikings have fought for their lives and survive another day..."
        elif vikingArmy == 1 and saxonArmy == 1:
            return "Vikings and Saxons are still the thick of the battle"


