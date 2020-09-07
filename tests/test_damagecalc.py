import damagecalc.damagecalc as damagecalc
import unittest

class TestDamageCalc(unittest.TestCase):

    def test_exception_is_raised_when_input_files_do_not_exist(self):
        damagecalc.main()