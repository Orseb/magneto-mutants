import unittest
from mutant_dna import is_mutant

class TestIsMutant(unittest.TestCase):

    def test_rows(self):
        dna = [
            ['A', 'A', 'A', 'A', 'T', 'G'],
            ['T', 'G', 'C', 'A', 'G', 'T'],
            ['G', 'C', 'T', 'T', 'C', 'C'],
            ['C', 'C', 'C', 'C', 'T', 'G'],
            ['G', 'T', 'A', 'G', 'T', 'C'],
            ['A', 'G', 'T', 'C', 'A', 'C']
        ]
        self.assertTrue(is_mutant(dna))

    def test_columns(self):
        dna = [
            ['A', 'G', 'A', 'A', 'T', 'G'],
            ['T', 'G', 'C', 'A', 'G', 'T'],
            ['G', 'C', 'T', 'T', 'C', 'C'],
            ['G', 'T', 'C', 'C', 'T', 'C'],
            ['G', 'T', 'A', 'G', 'T', 'C'],
            ['G', 'G', 'T', 'C', 'A', 'C']
        ]
        self.assertTrue(is_mutant(dna))

    def test_main_diagonals(self):
        dna = [
            ['A', 'G', 'A', 'A', 'T', 'G'],
            ['T', 'A', 'C', 'A', 'G', 'T'],
            ['G', 'C', 'A', 'G', 'C', 'C'],
            ['T', 'T', 'G', 'A', 'T', 'G'],
            ['G', 'T', 'A', 'G', 'T', 'C'],
            ['A', 'G', 'T', 'C', 'A', 'A']
        ]
        self.assertTrue(is_mutant(dna))

    def test_secondary_left_diagonals(self):
        dna = [
            ['A', 'T', 'A', 'A', 'T', 'G'],
            ['G', 'T', 'T', 'A', 'G', 'T'],
            ['G', 'G', 'C', 'T', 'C', 'G'],
            ['T', 'T', 'G', 'A', 'T', 'G'],
            ['G', 'T', 'A', 'G', 'T', 'C'],
            ['A', 'G', 'T', 'C', 'A', 'A']
        ]
        self.assertTrue(is_mutant(dna))

    def test_secondary_right_diagonals(self):
        dna = [
            ['A', 'T', 'A', 'A', 'T', 'G'],
            ['G', 'T', 'A', 'T', 'G', 'A'],
            ['G', 'C', 'T', 'T', 'A', 'G'],
            ['T', 'T', 'T', 'A', 'G', 'G'],
            ['G', 'T', 'A', 'G', 'T', 'C'],
            ['A', 'G', 'T', 'C', 'A', 'A']
        ]
        self.assertTrue(is_mutant(dna))

    def test_tertiary_left_diagonals(self):
        dna = [
            ['A', 'T', 'G', 'A', 'T', 'G'],
            ['G', 'T', 'A', 'G', 'T', 'A'],
            ['C', 'C', 'T', 'T', 'G', 'G'],
            ['T', 'C', 'T', 'A', 'G', 'G'],
            ['G', 'G', 'C', 'G', 'T', 'C'],
            ['A', 'G', 'T', 'C', 'A', 'A']
        ]
        self.assertTrue(is_mutant(dna))

    def test_tertiary_right_diagonals(self):
        dna = [
            ['A', 'T', 'G', 'A', 'T', 'G'],
            ['G', 'T', 'A', 'T', 'T', 'A'],
            ['A', 'A', 'T', 'T', 'G', 'G'],
            ['A', 'C', 'T', 'A', 'G', 'T'],
            ['G', 'G', 'A', 'G', 'T', 'C'],
            ['A', 'G', 'G', 'C', 'A', 'A']
        ]
        self.assertTrue(is_mutant(dna))

    def test_non_mutant(self):
        dna = [
            ['A', 'T', 'G', 'A', 'T', 'G'],
            ['G', 'T', 'C', 'T', 'T', 'A'],
            ['A', 'A', 'T', 'T', 'G', 'G'],
            ['A', 'C', 'T', 'A', 'G', 'T'],
            ['G', 'G', 'A', 'T', 'T', 'C'],
            ['A', 'G', 'G', 'C', 'A', 'A']
        ]
        self.assertFalse(is_mutant(dna))

if __name__ == '__main__':
    unittest.main()
