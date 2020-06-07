from helper import run_task
from unittest import TestCase, main

# Выводит всю информацию по государству
class Test03(TestCase):

    def setUp(self):
        self.t = lambda v: run_task('215', '3', v)
        self.e = lambda a, b: self.assertEqual(self.t(a), b)

    def test_russia(self):
        self.e('Russia', 'Moscow\n333\n333\nEurope\n')

    def test_germania(self):
        self.e('Germania', 'Berlin\n333\n333\nEurope\n')

