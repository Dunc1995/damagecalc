import unittest
import damagecalc.damagecalc as damagecalc

class TestDamageCalc(unittest.TestCase):

    def test_exception_is_raised_when_input_file_does_not_exist(self):
        #Assume
        file_path = './none_existent_file.csv'

        #Assert
        with self.assertRaises(FileNotFoundError) as fnfe:
            damagecalc.check_file_exists(file_path)

    def test_exception_is_raised_when_file_is_not_csv(self):
        #Assume
        file_path = './not_a_csv.txt'

        #Assert
        with self.assertRaises(Exception) as ncsv:
            damagecalc.check_is_file_csv(file_path)