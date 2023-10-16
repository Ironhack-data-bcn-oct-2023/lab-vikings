import random

# Soldier
class Soldier:
    # Initialize a Soldier with health and strength attributes.
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    #Soldier attack, returning their strength.
    def attack(self):
        return self.strength
    
    #Soldier takes damage
    def receiveDamage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    #Viking inherits from Soldier, re-initialize because also takes 'name' property
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    #Re-defines Soldier damage. Viking receives damage and return istring. If dead return the propper string
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    #Define a special method for Vikings to use a special attack.
    def battleCry(self):
        if random.random() <= 0.33:  # 33% chance for the special attack
            damage = random.randint(2, 10) #Randomly applyy between 2 and 10 damage
            return f"📣 {self.name} has used 'battle cry' -Odin owns you all!-\n    ⚔️ Inflicts {damage} points of damage to each Saxon"
        return ""

# Saxon
class Saxon(Soldier):
    #Saxon inherits from Soldier, no need to re-initialize

    #Re-defines Soldier damage. Saxon receives damage and return istring. If dead return the propper string
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

    #Define a special method for Vikings to use a special attack.
    def reinforcement(self, war):
        if random.random() <= 0.1:  #10% chance for the special attack
            num_reinforcements = random.randint(2, 10) #Randomly add between 2 and 10 weaker Saxons to the army with health 10 to 20 and strenght 1 to 3
            for _ in range(num_reinforcements): #Loop to trigger the addSaxon() method from War
                war.addSaxon(Saxon(random.randint(10, 20), random.randint(1, 3)))
            return f"❗ A sneaky Saxon has called for reinforcement.\n    🛡️ {num_reinforcements} weaker Saxons joined the battle"
        return ""
# War
class War:
    #Initialize war with the armys
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    #Add Viking/Saxon instances to each army
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    #Viking attack
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy) #Random select the Viking and the Saxon being attacked
        viking = random.choice(self.vikingArmy)

        # Calculate the result of the attack and any special attck effects.
        result = saxon.receiveDamage(viking.attack())
        battle_cry_result = viking.battleCry()
        if battle_cry_result:
            result += "\n" + battle_cry_result #Special attack result

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon) #If dead remove Saxon from army

        return result

    def saxonAttack(self):
        viking = random.choice(self.vikingArmy) #Random select the Saxon and the Viking being attacked
        saxon = random.choice(self.saxonArmy)

        # Calculate the result of the attack and any special attck effects.
        result = viking.receiveDamage(saxon.attack())
        reinforcement_result = saxon.reinforcement(self)  # Pass the War object.
        if reinforcement_result:
            result += "\n" + reinforcement_result #Special attack result

        if viking.health <= 0:
            self.vikingArmy.remove(viking) #If dead remove Viking from army

        return result

    #Return the status of the battle. If any of the two armys empty returns the winner
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
