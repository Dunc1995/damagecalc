import unittest
import damagecalc.utilities as utils
from os.path import join


class TestUtilities(unittest.TestCase):
    def setUp(self):
        #region #? csv input paths
        self.test_data_root = './tests/data'
        self.inconsistent_data_rows = join(
            self.test_data_root, 'inconsistent_data_rows.csv')
        self.non_numerical_values = join(
            self.test_data_root, 'non_numerical_values.csv')
        self.out_of_range_values = join(
            self.test_data_root, 'out_of_range_values.csv')

        self.normal_vulnerability_curve = join(
            self.test_data_root, 'normal_vulnerability_curve.csv')
        self.nonsense_vulnerability_curve = join(
            self.test_data_root, 'nonsense_vulnerability_curve.csv')
        #endregion

        self.vulnerability_curve_class = utils.vulnerability_curve(
            self.normal_vulnerability_curve)

        self.test_output = join(self.test_data_root, 'testing.csv')

    def test_value_error_is_raised_when_unusual_row_length_is_found(self):

        with self.assertRaises(ValueError) as value_error:
            utils.calculate_damage_costs(
                self.inconsistent_data_rows, self.test_output, self.vulnerability_curve_class)

    def test_value_error_is_raised_when_non_numeric_is_found(self):

        with self.assertRaises(ValueError) as value_error:
            utils.calculate_damage_costs(
                self.non_numerical_values, self.test_output, self.vulnerability_curve_class)

    def test_exception_is_raised_when_invalid_data_is_passed_to_vulnerability_curve(self):

        with self.assertRaises(ValueError) as value_error:
            utils.vulnerability_curve(self.nonsense_vulnerability_curve)
