import logging
import json
import csv


class vulnerability_curve():
    def __init__(self, input_obj):
        csv_rows = None

        if type(input_obj) is str:
            csv_rows = self.__get_list_from_csv(input_obj)
        elif type(input_obj) is list:
            csv_rows = input_obj
        
        self.depth_ranges = self.__validate_and_get_depth_ranges(csv_rows)
        self.min, self.max = self.__get_min_and_max_values()

    # ? Probably the most straightforward approach.
    def get_flood_damage_value(self, depth):
        '''Iterates through all of the curve\'s depth ranges and assigns a cost value to the input depth.'''
        i = 0

        cost_value = None
        for row in self.depth_ranges:  # ! This is definitely a bottleneck.
            is_in_range = self.__is_value_in_range(row[0], row[1], depth)
            if is_in_range == True:
                cost_value = float(self.depth_ranges[i][2])
                break
            i += 1

        if cost_value == None:
            logging.warning(
                'depth value of {} doesn\'t have an assigned cost.'.format(depth))

        return cost_value

    def __validate_and_get_depth_ranges(self, input_data: list):
        '''Returns None if any data row is not of length 3 - otherwise, returns the input list.'''
        output = None

        # ? If any rows are not of length 3.
        if any(not len(row) == 3 for row in input_data):
            raise ValueError(
                'Row lengths of 3 are required to instantiate a vulnerability_curve object.')
        else:
            output = input_data

        return output

    def __get_min_and_max_values(self):
        '''Gets the upper bound and lower bound for the vulnerability curve.'''

        all_values = []
        for row in self.depth_ranges:
            all_values.append(row[0])
            all_values.append(row[1])

        return min(all_values), max(all_values)

    def __get_list_from_csv(self, file_path: str, newline='', starting_index=1):
        '''Reads a csv file and returns its contents as a list object.'''
        output = []

        try:
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                # ? Starting index omits the headings from the csv
                for row in list(reader)[starting_index:]:
                    output.append(row)
        except Exception as e:
            raise Exception('Unable to read {}: {}'.format(file_path, str(e)))

        return output

    def __is_value_in_range(self, lower_limit: int, upper_limit: int, depth):
        '''Tests whether a given depth value is within the specified integer range. Returns true or false.'''
        lower_limit_float = float(lower_limit)
        upper_limit_float = float(upper_limit)
        depth_float = float(depth)

        if lower_limit_float > upper_limit_float:
            raise Exception(
                'Error at __is_value_in_range - your lower limit cannot be greater than your upper limit!\n lower_limit: {}, upper_limit: {}'.format(lower_limit, upper_limit))
        in_range = lower_limit_float < depth_float <= upper_limit_float

        logging.debug({'lower_limit': lower_limit_float,
                       'upper_limit': upper_limit_float, 'depth': depth, 'in_range': in_range})

        return in_range


def calculate_damage_costs(file_path: str, output_file: str, curve: vulnerability_curve, newline='', starting_index=1):
    '''Reads depth values from file_path and cross references the input vulnerability curve ranges for every row. The output values can be found in out_put_file'''
    cost_output = 0
    count = 0

    with open(output_file, 'w', newline='') as fo:
        fieldnames = ['depth', 'damage_cost']
        writer = csv.DictWriter(fo, fieldnames=fieldnames)
        writer.writeheader()

        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            for row in list(reader)[starting_index:]:
                if len(row) > 1:
                    raise ValueError(
                        'Depth value files should only contain one column. Instead found row with {} elements.'.format(len(row)))

                result = curve.get_flood_damage_value(row[0])
                writer.writerow({'depth': row[0], 'damage_cost': result})
                cost_output += result
                count += 1

    return cost_output, count
