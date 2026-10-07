import unittest
from random_words import get_words_recursive, get_words_iterative


class RandomWordsTest(unittest.TestCase):
    def setUp(self):
        self.cases = [
            # (word_size, letters, [words...])
            (1, 'ab', ['a', 'b']),
            (2, 'set', ['ss', 'se', 'st', 'es', 'ee', 'et', 'ts', 'te', 'tt']),
            (5, 'a', ['aaaaa']),
            (4, 'ab', ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']),
        ]

    def test_recursive(self):
        for (count, letters, result) in self.cases:
            self.assertEqual(sorted(get_words_recursive(count, letters)), sorted(result))

    def test_iterative(self):
        for (count, letters, result) in self.cases:
            self.assertEqual(sorted(get_words_iterative(count, letters)), sorted(result))


if __name__ == '__main__':
    unittest.main()
