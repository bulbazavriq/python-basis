from helper import run_task
from unittest import TestCase, main

class Test01(TestCase):

    def test_russia(self):
        self.assertEqual(run_task('215', '1', 'Russia'), 'Moscow\n')
    def test_germania(self):
        self.assertEqual(run_task('215', '1', 'Germania'), 'Berlin\n')
    def test_undefined(self):
        self.assertEqual(run_task('215', '1', 'Xiaomi'), '')

if __name__ == '__main__':
    main()
