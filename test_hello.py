import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(greet("Claude"), "Hello, Claude!")


if __name__ == "__main__":
    unittest.main()
