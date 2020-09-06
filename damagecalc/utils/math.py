import logging
import json

class vulnerability_curve():
    def __init__(self, input_data: list):
        try:
            if any(not len(row) == 3 for row in input_data): #? If any rows are not of length 3.
                raise Exception('Row lengths of 3 are required to instantiate a vulnerability_curve object.')
            else:
                self.raw_data = input_data #! This assignment may cause mutability issues as it's effectively an input by reference.
        except Exception as e:
            logging.fatal(str(e))

    def get_flood_damage_value(self, depth): #? Probably the most straightforward approach.
        '''Iterates through all of the curve\'s depth ranges and assigns a cost value to the input depth.'''
        i = 0
        cost_value = None
        for row in self.raw_data: #! This is definitely a bottleneck.
            is_in_range = self.__is_value_in_range(row[0], row[1], depth)
            if is_in_range == True:
                cost_value = float(self.raw_data[i][2])
                break            
            i += 1

        if cost_value == None:
            logging.warning('depth value of {} doesn\'t have an assigned cost.'.format(depth))

        return cost_value

    def __is_value_in_range(self, lower_limit: int, upper_limit: int, depth):
        '''Tests whether a given depth value is within the specified integer range. Returns true or false.'''
        lower_limit_float = float(lower_limit)
        upper_limit_float = float(upper_limit)
        depth_float = float(depth)

        if lower_limit_float > upper_limit_float:
            raise Exception('Error at __is_value_in_range - your lower limit cannot be greater than your upper limit!\n lower_limit: {}, upper_limit: {}'.format(lower_limit, upper_limit))
        in_range = lower_limit_float < depth_float <= upper_limit_float

        logging.debug({ 'lower_limit': lower_limit_float, 'upper_limit': upper_limit_float, 'depth': depth, 'in_range': in_range })

        return in_range

    #TODO Test the performance of the key-value pair approach versus the standard if statement approach:
    #? This function could be used to create keys for every cost vs depth range. A possible bottleneck
    #? with this approach would then be using math.floor and math.ceiling to obtain the right key
    #? from each depth value; would need to profile this approach's performance to justify its use.
    def create_key_value_pairs(self):
        for row in self.raw_data:
            self.__setattr__(str(row[0] + row[1]), row[2]) #? Sets a key-value pair for each depth range and its respective amount of damage.
        logging.debug('vulnerability_curve object:')
        logging.debug(json.dumps(self.__dict__, indent=4))