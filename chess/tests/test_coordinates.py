import unittest
from chess.chess_exceptions import NotValidCoordinate, NotValidCoordinateOffset
from chess.coordinates import Coordinate


class CoordinatesTest(unittest.TestCase):
    def test_create_coordinate(self):
        self.assertEqual(str(Coordinate("a", 2)), "a2")

    def test_create_coordinate_upper(self):
        self.assertEqual(str(Coordinate("C", 2)), "c2")

    def test_create_invalid_coordinate_file(self):
        with self.assertRaises(NotValidCoordinate):
            Coordinate("m", 1)

    def test_create_invalid_coordinate_rank(self):
        with self.assertRaises(NotValidCoordinate):
            Coordinate("a", 0)


if __name__ == '__main__':
    unittest.main()
