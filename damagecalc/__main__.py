import argparse
import logging
import os

def main():
    '''Entry point for the damage calculator script'''
    parser = argparse.ArgumentParser(description='Tool for calculating the expected £\'s of damage for a quantifiable level of flood risk.')
    parser.add_argument('--log_verbosity', '-v', type=int, default=2, help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()

# def write_to_file(file_path: str, contents: str):
#     with open(file_path, 'w+') as file:
#         file.write(contents)
#         file.close()

def value_in_range(lower_limit: int, upper_limit: int, depth):
    '''Tests whether a given depth value is within the specified range'''

    if lower_limit > upper_limit:
        raise Exception('Error at value_in_range - your lower limit cannot be greater than your upper limit!')
    in_range = lower_limit < depth < upper_limit
    
    return in_range


if __name__ == "__main__":
    main()
    