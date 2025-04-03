import unittest
from velociraptor import Velociraptor
from thescelosaurus import Thescelosaurus
import math
from utility import Direction

class TestVelociraptor(unittest.TestCase):

    def test_setOrien(self):
        v = Velociraptor([1,1])
        v.orientation = 7 *math.pi
        self.assertTrue(v.orientation <= 2 * math.pi,f"{v.orientation}")

    def test_setAngVelo(self):
        v = Velociraptor([1,1])
        v.angular_velocity = 100
        self.assertTrue(v.angular_velocity<100)

    def test_findWantAng(self):
        v = Velociraptor([1,1])
        self.assertEqual(v._find_wanted_angle([0,0]), 5/4*math.pi)
        self.assertEqual(v._find_wanted_angle([2,1]),0)

    def test_findOri(self):
        v = Velociraptor([1,1],math.pi/2)
        self.assertEqual(v._find_orientation(5*(math.pi/4)), Direction.LEFT)
        self.assertEqual(v._find_orientation(7*(math.pi)/4), Direction.RIGHT)

    def test_fonctionx(self):
        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()
