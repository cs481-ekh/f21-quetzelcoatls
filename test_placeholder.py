from unittest import TestCase
from placeholder import Placeholder

class TestPlaceholder(TestCase):
    def test_add(self):
        self.assertEqual(Placeholder.add(2, 2), 4)
