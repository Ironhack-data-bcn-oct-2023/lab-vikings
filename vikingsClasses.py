
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = 300
        self.strength = 150
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage
        return None

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = "Harald"
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        self.battleCry
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__(health, strength)
        self.health = 60
        self.strength = 25
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        return None
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        return None
    
    
    def vikingAttack(self):
        dead_saxons = 0
        for saxon in self.saxonArmy:
            damage = self.vikingArmy[0].strength
            saxon.receiveDamage(damage)
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
                dead_saxons += 1
                return 'A Saxon has died in combat'
            else: 
                return f'A Saxon has received {damage} points of damage'
    
    def saxonAttack(self):
        dead_vikings = 0
        for viking in self.vikingArmy:
            damage = self.saxonArmy[0].strength
            viking.receiveDamage(damage)
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
                dead_vikings +=1
                return 'Harald has died in combat'
            else:
                return f'Harald has received {damage} points of damage'
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
    



        
