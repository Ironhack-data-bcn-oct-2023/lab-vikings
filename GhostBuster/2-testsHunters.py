import unittest
from GhostBuster import Hunters
from inspect import signature


class TestHunters(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.name = 'Fernando'
        cls.strength = 150
        cls.health = 300
        cls.hunters = Hunters(cls.name, cls.health, cls.strength)

    def testShouldReciveThreeParams(self):
        self.assertEqual(len(signature(Hunters).parameters), 3)

    def testName(self):
        self.assertEqual(self.hunters.name_team1, self.name)

    def testHealth(self):
        self.assertEqual(self.hunters.health, self.health)

    def testStrenght(self):
        self.assertEqual(self.hunters.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.hunters.attack), True)

    def testAttackReciveNoParameters(self):
        self.assertEqual(len(signature(self.hunters.attack).parameters), 0)

    def testAttackShouldReturnStrength(self):
        self.assertEqual(self.hunters.attack(), self.strength)

    def testReceiveDamageIsFunction(self):
        self.assertEqual(callable(self.hunters.receiveDamage), True)

    def testReceiveDamageReciveOneParam(self):
        self.assertEqual(
            len(signature(self.hunters.receiveDamage).parameters), 1)

    def testReciveDamageShouldRestHealth(self):
        self.hunters.receiveDamage(50)
        self.assertEqual(self.hunters.health, self.health - 50)

    def testReciveDamageShouldReturnString50(self):
        self.assertEqual(self.hunters.receiveDamage(50), self.name +
                         ' has received 50 points of damage')

    def testReciveDamageShouldReturnString70(self):
        self.assertEqual(self.hunters.receiveDamage(70), self.name +
                         ' has received 70 points of damage')

    def testReceiveDamageShouldReturnStringDeath(self):
        self.assertEqual(self.hunters.receiveDamage(self.health),
                         self.name + ' has died in act of combat')

    def testBattleCry(self):
        self.assertEqual(callable(self.hunters.battleCry), True)

    def testBattleCryReturnString(self):
        self.assertEqual(self.hunters.battleCry(), 'For Glory and Victory!')


if __name__ == '__main__':
    unittest.main()
