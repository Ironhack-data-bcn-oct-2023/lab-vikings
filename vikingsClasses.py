
import random
# Soldier
class Soldier:

    '''Soldier:
       A class to generate a soldier object with health and strength params:
       
    Attributes
    ----------
    health : int
        level of health of a soldier
    strength : int
        level of strength of a soldier.
    Methods
    --------------------------------------
    attack()
        it returns strength of a soldier. This strength will be damage in enemy
    receiveDamage(damage)
        It substract level of damage (strength enemy) to soldier under attack
    '''

    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage

# Viking

'''Viking (inheritance of Soldier):
       Build a new viking soldier
       
    Attributes
    ----------
    health : int
        level of health of a soldier
    strength : int
        level of strength of a soldier.

    Methods
    --------------------------------------
    receiveDamage(damage)
        It substract level of damage (strength enemy) to soldier under attack 
        but we control level of health to check damage or to assign as dead soldier
    
    battleCry()
        Just a message from god Odin!
'''

class Viking(Soldier):
    
    def __init__(self,name,health,strength):  
        self.name = name
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health-damage
        if self.health > 0:
           return f"{self.name} has received {self.damage} points of damage"
        else:
           return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
        


# Saxon

'''Saxon (inheritance of Soldier):
       Build a new viking soldier
       
    Attributes
    ----------
    health : int
        level of health of a soldier
    strength : int
        level of strength of a soldier.

    Methods
    --------------------------------------
    receiveDamage(damage)
        It substract level of damage (strength enemy) to soldier under attack 
        but we control level of health to check damage or to assign as dead soldier
    
'''
class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage

        if self.health > 0:
           return f"A Saxon has received {self.damage} points of damage"
        else:
           return "A Saxon has died in combat"


# War

'''War ():
       Time for clash. 1:1 fight Viking vs Saxon.

    Methods
    --------------------------------------
    addViking(Viking)
        Using class Viking we instantiate a viking soldier object and it will be added
        to viking army as part of a list of soldiers.

    addSaxon(Saxon)
        Using class Saxon we instantiate a saxon soldier object and it will be added
        to saxon army as part of a list of soldiers.

    vikingAttack()
        we pick a viking from it's army and he will clash against a saxon soldier.
        Saxon soldier will receive viking strength as damage and if its health is equals or less than 0 
        saxon will die and he will be removed from saxon army
    
    saxonAttack()
        we pick a saxon from it's army and he will clash against a viking soldier.
        Viking soldier will receive saxon strength as damage and if its health is equals or less than 0 
        viking will die and he will be removed from viking army

    showStatus()
        status of the battle. It will show a sentence about who wins.

'''

class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []  

    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        e_saxon = random.choice(self.saxonArmy)
        e_viking = random.choice(self.vikingArmy)

        v_damage = e_saxon.receiveDamage(e_viking.strength)

        if e_saxon.health <= 0:
            self.saxonArmy.remove(e_saxon)
        return v_damage
    
    def  saxonAttack(self):
        e_saxon = random.choice(self.saxonArmy)
        e_viking = random.choice(self.vikingArmy)

        v_damage = e_viking.receiveDamage(e_saxon.strength)
        
        if e_viking.health <= 0:
            self.vikingArmy.remove(e_viking)

        return v_damage
    
    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            return("Vikings have won the war of the century!")
        elif len(self.vikingArmy)==0:
            return("Saxons have fought for their lives and survive another day...")
        else:
            return "Vikings and Saxons are still in the thick of battle."



