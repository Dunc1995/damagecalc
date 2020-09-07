import unittest
import damagecalc.utilities as utils
import os

class TestUtilities(unittest.TestCase):
    def setUp(self):
        self.test_data_root = './tests/data'
        self.inconsistent_data_rows = os.path.join(self.test_data_root, 'inconsistent_data_rows.csv')
        self.non_numerical_values = os.path.join(self.test_data_root, 'non_numerical_values.csv')
        self.normal_vulnerability_curve = os.path.join(self.test_data_root, 'normal_vulnerability_curve.csv')
        self.out_of_range_values = os.path.join(self.test_data_root, 'out_of_range_values.csv')
        self.test_output = os.path.join(self.test_data_root, 'testing.csv')

        self.vulnerability_curve_class = utils.vulnerability_curve(self.normal_vulnerability_curve)

    def test_value_error_is_raised_when_unusual_row_length_is_found(self):

            with self.assertRaises(ValueError) as value_error:
                utils.calculate_damage_costs(self.inconsistent_data_rows, self.test_output, self.vulnerability_curve_class.get_flood_damage_value)

    def test_value_error_is_raised_when_non_numeric_is_found(self):

        with self.assertRaises(ValueError) as value_error:
            utils.calculate_damage_costs(self.non_numerical_values, self.test_output, self.vulnerability_curve_class.get_flood_damage_value)