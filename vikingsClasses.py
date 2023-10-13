
# Soldier


class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        
        pass
        

# Viking


class Viking(Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage."
        else: 
            return f"{self.name} has died in act of combat."

    def battleCry(self):
        return "Odin Owns You All!"

    pass

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else: 
            return "A Saxon has died in combat"

    pass

# War

import random
class War(Viking, Saxon):
    def __init__(self):
        self.VikingArmy = []
        self.SaxonArmy = []
        pass

    def addViking(self, Viking):
        self.VikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.SaxonArmy.append(Saxon)


    def VikingAttack(self):
       
        random_Saxon = random.randint(0, len(self.SaxonArmy)-1)
        Saxon: Saxon = self.SaxonArmy[random_Saxon]

        random_Viking = random.randint(0, len(self.VikingArmy)-1)
        Viking: Viking = self.VikingArmy[random_Viking]

        Saxon_damage = Saxon.receiveDamage(Viking.attack())
        if Saxon.health <= 0:
            self.SaxonArmy.remove(Saxon)
        return Saxon_damage
    
    def SaxonAttack(self):
       
        random_Saxon = random.randint(0, len(self.SaxonArmy)-1)
        Saxon: Saxon = self.SaxonArmy[random_Saxon]

        random_Viking = random.randint(0, len(self.VikingArmy)-1)
        Viking: Viking = self.VikingArmy[random_Viking]

        Viking_damage = Viking.receiveDamage(Saxon.attack())
        if Viking.health <= 0:
            self.VikingArmy.remove(Viking)
        return Viking_damage     
    
    def showStatus(self):

        for i in self.VikingArmy:
            if len(self.VikingArmy) == 0:
                return Saxons have fought for their lives and survive another day...
            elif len(self.SaxonArmy) == 0:
                return Vikings have won the war of the century!
            else: 
                return Vikings and Saxons are still in the thick of battle.    




    pass
