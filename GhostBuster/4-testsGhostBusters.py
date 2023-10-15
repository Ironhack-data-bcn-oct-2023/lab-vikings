import unittest
from GhostBuster import GhostBusters, Hunters, Ghosts


class TestGhostBusters(unittest.TestCase):
    def testHunterAttack(self):
        ghostbusters = GhostBusters([], [])
        result = ghostbusters.hunterAttack()
        self.assertEqual(result, "There are no ghosts left to attack.")

    def testGhostAttack(self):
        ghostbusters = GhostBusters([], [])
        result = ghostbusters.ghostAttack()
        self.assertEqual(result, "There are no hunters left to possess.")

    def testShowStatusHuntersWin(self):
        ghostbusters = GhostBusters(["Ghost1", "Ghost2"], [])
        result = ghostbusters.showStatus()
        self.assertEqual(result, "Hunters have won the hunting of the century")

    def testShowStatusGhostsWin(self):
        ghostbusters = GhostBusters([], ["Hunter1", "Hunter2"])
        result = ghostbusters.showStatus()
        self.assertEqual(result, "Ghosts have possessed the bodies of hunters")

    def testShowStatusStillFighting(self):
        ghostbusters = GhostBusters(["Hunter1", "Hunter2"], ["Ghost1", "Ghost2"])
        result = ghostbusters.showStatus()
        self.assertEqual(result, "Hunters and Ghosts are still in the thick of battle!!")

class TestHunters(unittest.TestCase):
    def testReceiveDamage(self):
        hunter = Hunters("Hunter1", 100, 50)
        result = hunter.receiveDamage(30)
        self.assertEqual(result, "Hunter1 has received 30 points of damage")

    def testBattleCry(self):
        hunter = Hunters("Hunter1", 100, 50)
        result = hunter.battleCry()
        self.assertEqual(result, "For Glory and Victory!")

class TestGhosts(unittest.TestCase):
    def testReceiveDamage(self):
        ghost = Ghosts("Ghost1", 100, 50)
        result = ghost.receiveDamage(30)
        self.assertEqual(result, "Ghost1 has received 30 points of damage")

    def testBattleCry(self):
        ghost = Ghosts("Ghost1", 100, 50)
        result = ghost.battleCry()
        self.assertEqual(result, "No Mercy, No Regrets!")

if __name__ == '__main__':
    unittest.main()
