import unittest
from GhostBuster import Ghosts
from inspect import signature


class TestGhosts(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.name = 'Bego'
        cls.health = 250
        cls.strength = 100
        cls.ghosts = Ghosts(cls.name, cls.health, cls.strength)

    def testShouldReciveThreeParams(self):
        self.assertEqual(len(signature(Ghosts).parameters), 3)

    def testName(self):
        self.assertEqual(self.ghosts.name_team2, self.name)
        
    def testHealth(self):
        self.assertEqual(self.ghosts.health, self.health)

    def testStrength(self):
        self.assertEqual(self.ghosts.strength, self.strength)

    def testAttack(self):
        self.assertEqual(callable(self.ghosts.attack), True)

    def testAttackShouldReceiveNoParams(self):
        self.assertEqual(len(signature(self.ghosts.attack).parameters), 0)

    def testAttackREturnStrength(self):
        self.assertEqual(self.ghosts.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.ghosts.receiveDamage), True)

    def testReceiveDamageShouldReceiveOneParam(self):
        self.assertEqual(
            len(signature(self.ghosts.receiveDamage).parameters), 1)

    def testReceiveDamage(self):
        self.ghosts.receiveDamage(1)
        self.assertEqual(self.ghosts.health, self.health - 1)

    def testReceiveDamageString45(self):
        self.assertEqual(self.ghosts.receiveDamage(
            45), self.name + ' has received 45 points of damage')

    def testReceiveDamageString10(self):
        self.assertEqual(self.ghosts.receiveDamage(
            10), self.name + ' has received 10 points of damage')

    def testReceiveDamageStringDied(self):
        self.assertEqual(self.ghosts.receiveDamage(self.health), 
                         self.name + ' has died in combat')

    def testBattleCry(self):
        self.assertEqual(callable(self.ghosts.battleCry), True)

    def testBattleCryReturnString(self):
        self.assertEqual(self.ghosts.battleCry(), 'No Mercy, No Regrets!')


if __name__ == '__main__':
    unittest.main()
