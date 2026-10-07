import unittest

from text_analysis import insert_spaces


class TestInsertSpaces(unittest.TestCase):

    def test_sngle_word_returns_same_word(self):
        dictionary = {"hello"}

        result = insert_spaces("hello", dictionary)

        self.assertEqual(result, "hello")

    def test_sentence_is_split_into_words(self):
        dictionary = {"hello", "world"}

        result = insert_spaces("helloworld", dictionary)

        self.assertEqual(result, "hello world")

    def test_prefers_longer_word_when_multipla_splits_are_possible(self):
        dictionary = {"to", "do", "todo", "list"}

        result = insert_spaces("todolist", dictionary)

        self.assertEqual(result, "todo list")

    def test_backtracks_when_longest_word_leads_to_dead_end(self):
        dictionary = {"abc", "ab", "cd"}

        result = insert_spaces("abcd", dictionary)

        self.assertEqual(result, "ab cd")

    def test_returns_none_when_no_solution_exists(self):
        dictionary = {"hello", "world"}

        result = insert_spaces("", dictionary)

        self.assertIsNone(result)

    def test_empty_sentence_returns_empty_string(self):
        dictionary = {"hello"}

        result = insert_spaces("", dictionary)

        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()
