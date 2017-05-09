from unittest import TestCase


class TestDocument(TestCase):
    def test_insert(self):
        pass

    def test_delete(self):
        pass

    def test_save(self):
        pass

    def test_forward(self):
        self.assertRaises(EOFError)

    def test_back(self):
        self.assertRaises(Exception)
