import unittest
from one_hot_encoder import fit_transform


class TestFitTransformSimple(unittest.TestCase):
    def testCorrSimple(self):
        self.assertEqual(
            [
                ("Moscow", [0, 0, 1]),
                ("New York", [0, 1, 0]),
                ("Moscow", [0, 0, 1]),
                ("London", [1, 0, 0]),
            ],
            fit_transform(["Moscow", "New York", "Moscow", "London"]),
        )

    def testCorrWithArgs(self):
        res = fit_transform(*["Moscow", "New York", "Moscow", "London"])
        self.assertNotIn(("Moscow", [0, 1, 1]), res)

    def testIncorWithoutArgs(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def testIncorArgTypes(self):
        with self.assertRaises(TypeError):
            fit_transform(1, 2, {3}, 4)


if __name__ == "__main__":
    unittest.main()
