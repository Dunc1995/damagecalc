import argparse
import logging
import os
import damagecalc.utils.csv as csv

def get_user_arguments():
    '''Lists the required/optional arguments for the damagecalc script and returns an args object.'''
    parser = argparse.ArgumentParser(description='Tool for calculating the expected £\'s of damage for a quantifiable level of flood risk.')
    parser.add_argument('--input_depths', '-i', type=str, help='Input .csv file for depth data.', required=True)
    parser.add_argument('--input_vulnerability_curve', '-c', type=str, help='Input .csv file for a vulnerability curve.', required=True)
    parser.add_argument('--log_verbosity', '-v', type=int, default=2, help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()

    return args

def main():
    '''Entry point for the damage calculator script.'''
    args = get_user_arguments()
    logging.basicConfig(filename='./damagecalc.log', filemode='w', level=args.log_verbosity*10) #? This will dump a log file wherever the user has navigated to.

    try: #? If an exception is raised at this point, you can assume that the application has failed.
        csv.get_dict_from_csv(args.input_depths)
        csv.get_dict_from_csv(args.input_vulnerability_curve)
        
    except Exception as e:
        exception_string = str(e)
        print(exception_string)
        logging.fatal(exception_string)
    