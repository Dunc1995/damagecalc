import unittest
import damagecalc.utilities as utils
from os.path import join


class TestUtilities(unittest.TestCase):
    def setUp(self):
        # region #? csv input paths
        self.test_data_root = './tests/data'

        self.normal_depths = join(
            self.test_data_root, 'normal_depths.csv')
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
        # endregion

        self.vulnerability_curve_class = utils.vulnerability_curve(
            self.normal_vulnerability_curve)

        self.test_output = join(self.test_data_root, 'testing.csv')

    def test_inconsistent_data_rows_are_counted_when_found(self):
        # Assume
        number_of_inconsistent_data_rows = 2

        # Action
        total_cost, count, erroneous_data_count = utils.calculate_damage_costs(
            self.inconsistent_data_rows, self.test_output, self.vulnerability_curve_class)

        # Assert
        self.assertEqual(number_of_inconsistent_data_rows,
                         erroneous_data_count)

    def test_out_of_range_values_are_counted_when_found(self):
        # Assume
        number_of_inconsistent_data_rows = 4

        # Action
        total_cost, count, erroneous_data_count = utils.calculate_damage_costs(
            self.out_of_range_values, self.test_output, self.vulnerability_curve_class)

        # Assert
        self.assertEqual(number_of_inconsistent_data_rows,
                         erroneous_data_count)

    def test_value_error_is_raised_when_non_numeric_is_found(self):

        with self.assertRaises(ValueError):
            utils.calculate_damage_costs(
                self.non_numerical_values, self.test_output, self.vulnerability_curve_class)

    def test_exception_is_raised_when_invalid_data_is_passed_to_vulnerability_curve(self):

        with self.assertRaises(ValueError):
            utils.vulnerability_curve(self.nonsense_vulnerability_curve)

    def test_min_and_max_values_are_returned_correctly_from_vulnerability_curve_data(self):
        # Assume
        example_curve_data = [
            [1, 2, 200],
            [2, 3, 400],
            [3, 4, 600],
            [4, 5, 800]
        ]

        # Action
        curve = utils.vulnerability_curve(example_curve_data)

        # Assert
        self.assertTrue(curve.max == 5)
        self.assertTrue(curve.min == 1)

    def test_exception_is_raised_when_curve_data_contains_string(self):
        # Assume
        example_curve_data = [
            [1, 2, 200],
            [2, 'a string', 400],
            [3, 4, 600],
            [4, 5, 800]
        ]

        # Assert
        with self.assertRaises(Exception):
            utils.vulnerability_curve(example_curve_data)
