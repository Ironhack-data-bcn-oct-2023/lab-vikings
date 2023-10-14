
# Soldier


from typing import Self


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):    
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
          return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return f"Odin Owns You All!"


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



# War
import random 

class War():
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)


#first !! attack
    def vikingAttack(self):
       if self.saxonArmy:
           Saxon = random.choice(self.saxonArmy)
           Viking = random.choice(self.vikingArmy)
           damage = Viking.attack()
           result = Saxon.receiveDamage(damage)
       if Saxon.health <= 0:
            self.saxonArmy = [i for i in self.saxonArmy if Saxon.health > 0]
            return result
       

#second !! attack
       
    def saxonAttack(self):
     if self.vikingArmy:
         saxon = random.choice(self.saxonArmy)
         viking = random.choice(self.vikingArmy)
         damage = saxon.attack()
         result = viking.receiveDamage(damage)
     if viking.health <= 0:
            self.vikingArmy.remove(viking)
            return result
     return result
    
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."