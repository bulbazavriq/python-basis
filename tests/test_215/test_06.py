from helper import run_task
from unittest import TestCase, main

class Test06(TestCase):

    def setUp(self):
        self.t = lambda v: run_task('215', '6', v)
        self.e = lambda a, b: self.assertEqual(self.t(a), b)

    def test_asia(self):
        self.e('Asia', '1\n')

    def test_europe(self):
        self.e('Europe', '4\n')

    def test_undefined(self):
        self.e('Xiaomi', '0\n')
