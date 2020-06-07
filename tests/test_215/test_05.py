from helper import run_task
from unittest import TestCase, main

class Test05(TestCase):

    def setUp(self):
        self.t = lambda v: run_task('215', '5', v)
        self.e = lambda a, b: self.assertEqual(self.t(a), b)

    def test_russia(self):
        self.e('Russia', '1\n')

    def test_china(self):
        self.e('China', '2\n')

    def test_undefined(self):
        self.e('Xiaomi', '')
