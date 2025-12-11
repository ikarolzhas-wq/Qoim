import unittest
from storehouse.parser_tools import check_python, lexical_analysis

class TestParser(unittest.TestCase):
    def test_lexical(self):
        code = "a = 5"
        tokens = lexical_analysis(code)
        self.assertIn("a", tokens)
        self.assertIn("5", tokens)

    def test_syntax_ok(self):
        status, msg = check_python("x = 10")
        self.assertTrue(status)

    def test_syntax_error(self):
        status, msg = check_python("x = ")
        self.assertFalse(status)
