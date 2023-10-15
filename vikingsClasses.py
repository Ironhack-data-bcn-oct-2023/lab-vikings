
import random as rd


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
        return "Odin Owns You All!"
        
        

# Saxon


class Saxon(Soldier):
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
            

# War


class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
            
    def addViking(self, Viking_obj):
        self.vikingArmy += [Viking_obj]
        
    def addSaxon(self, Saxon_obj):
        self.saxonArmy += [Saxon_obj]
        
    def vikingAttack(self):
        saxon_rand = self.saxonArmy[rd.randint(0,len(self.saxonArmy)-1)]
        viking_rand = self.vikingArmy[rd.randint(0,len(self.vikingArmy)-1)]
        

        
        if saxon_rand.health <= viking_rand.attack():
            self.saxonArmy.remove(saxon_rand)
            
        return  saxon_rand.receiveDamage(viking_rand.attack())
    
    
    
    def saxonAttack(self):
        viking_rand = self.vikingArmy[rd.randint(0,len(self.vikingArmy)-1)]
        saxon_rand = self.saxonArmy[rd.randint(0,len(self.saxonArmy)-1)]
                  
        if viking_rand.health <= saxon_rand.attack():
            self.vikingArmy.remove(viking_rand)
            
        return viking_rand.receiveDamage(saxon_rand.attack()) 
    
    def showStatus(self):
        
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."  
