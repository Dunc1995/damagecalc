def value_in_range(lower_limit: int, upper_limit: int, depth):
    '''Tests whether a given depth value is within the specified range'''

    if lower_limit > upper_limit:
        raise Exception('Error at value_in_range - your lower limit cannot be greater than your upper limit!')
    in_range = lower_limit < depth < upper_limit
    
    return in_range