from helper import run_task
from unittest import TestCase, main

# Находит столицу для государства
class Test01(TestCase):

    def setUp(self):
        self.t = lambda v: run_task('215', '1', v)
        self.e = lambda a, b: self.assertEqual(self.t(a), b)

    def test_russia(self):
        self.e('Russia', 'Moscow\n')
    def test_germania(self):
        self.e('Germania', 'Berlin\n')
    def test_undefined(self):
        self.e('Xiaomi', '')
