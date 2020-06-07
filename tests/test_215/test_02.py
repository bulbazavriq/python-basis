from helper import run_task
from unittest import TestCase, main

class Test02(TestCase):

    def setUp(self):
        self.t = lambda v: run_task('215', '2', v)
        self.e = lambda a, b: self.assertEqual(self.t(a), b)

    def test_russia(self):
        self.e('Moscow', 'Russia\n')
    def test_germania(self):
        self.e('Berlin', 'Germania\n')
    def test_undefined(self):
        self.e('Xiaomi', '')

if __name__ == '__main__':
    main()
