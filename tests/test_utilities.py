import unittest
import damagecalc.utilities as utils
import os

class TestUtils(unittest.TestCase):
    def __init__(self):
        self.test_data_root = './data'
        self.inconsistent_data_rows = os.path.join(self.test_data_root, 'inconsistent_data_rows.csv')
        self.non_numerical_values = os.path.join(self.test_data_root, 'non_numerical_values.csv')
        self.normal_vulnerability_curve = os.path.join(self.test_data_root, 'normal_vulnerability_curve.csv')
        self.out_of_range_values = os.path.join(self.test_data_root, 'out_of_range_values.csv')
        self.vulnerability_curve_class = utils.vulnerability_curve(self.normal_vulnerability_curve)

    def test_value_error_is_raised_when_unusual_row_length_is_found(self):

            #Assert
            with self.assertRaises(ValueError) as value_error:
                utils.calculate_damage_costs(self.inconsistent_data_rows_path, self.vulnerability_curve_class.get_flood_damage_value)