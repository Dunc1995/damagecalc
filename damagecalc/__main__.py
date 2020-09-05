import argparse
import logging
import os
import damagecalc.utils.csv as csv

def user_arguments():
    '''Lists the required/optional arguments for the damagecalc script and returns an args object.'''
    parser = argparse.ArgumentParser(description='Tool for calculating the expected £\'s of damage for a quantifiable level of flood risk.')
    parser.add_argument('--input_depths', '-i', type=str, help='Input .csv file for depth data.', required=True)
    parser.add_argument('--input_vulnerability_curve', '-c', type=str, help='Input .csv file for a vulnerability curve.', required=True)
    parser.add_argument('--log_verbosity', '-v', type=int, default=2, help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()

    return args

def main():
    '''Entry point for the damage calculator script.'''
    args = user_arguments()
    csv.get_dict_from_csv(args.input_depths)
    csv.get_dict_from_csv(args.input_vulnerability_curve)

if __name__ == "__main__":
    main()
    