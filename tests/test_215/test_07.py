from helper import run_task
from unittest import TestCase, main

# Выводит суммарную площадь государств указанной части света
class Test07(TestCase):

    def setUp(self):
        self.t = lambda v: run_task('215', '7', v)
        self.e = lambda a, b: self.assertEqual(self.t(a), b)

    def test_asia(self):
        self.e('Asia', '500\n')

    def test_europe(self):
        self.e('Europe', '1332\n')

    def test_undefined(self):
        self.e('Xiaomi', '0\n')

