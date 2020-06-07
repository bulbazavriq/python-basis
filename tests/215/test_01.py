from helper import run_task
from unittest import TestCase, main

class Test01(TestCase):
    def test_moscow(self):
        self.assertEqual(run_task('215', '1', 'Moscow'), 'Russia')

