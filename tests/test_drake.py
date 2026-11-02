# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
import drake

class DrakeTests(unittest.TestCase):
    def test_historical_defaults(self):
        self.assertAlmostEqual(drake.estimate(drake.DrakeParameters()), 0.000005)
    def test_zero_fraction(self):
        p = drake.DrakeParameters(fraction_developing_life=0)
        self.assertEqual(drake.estimate(p), 0)
    def test_invalid_fraction(self):
        with self.assertRaises(ValueError):
            drake.estimate(drake.DrakeParameters(fraction_with_planets=1.5))
    def test_nan(self):
        with self.assertRaises(ValueError):
            drake.estimate(drake.DrakeParameters(detectable_years=float("nan")))

if __name__ == "__main__":
    unittest.main()
