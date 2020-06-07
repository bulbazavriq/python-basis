from helper import run_task
from unittest import TestCase, main

class Test04(TestCase):

    def setUp(self):
        self.t = lambda v: run_task('215', '4', v)
        self.e = lambda a, b: self.assertEqual(self.t(a), b)

    def test_europe(self):
        self.e('Europe', 'Russia\nFrancia\nGermania\nItalia\n')

    def test_asia(self):
        self.e('Asia', 'China\n')

    def test_undefined(self):
        self.e('Xiaomi', '')
