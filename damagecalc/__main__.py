import argparse
import logging
import damagecalc.utilities as utils


def get_arguments():
    '''Lists the required/optional arguments for the damagecalc script and returns an args object.'''

    parser = argparse.ArgumentParser(
        description='Tool for calculating the expected £\'s of damage for a quantifiable level of flood risk.')
    parser.add_argument('--input_depths', '-d', type=str,
                        help='Input .csv file for depth data.', required=True)
    parser.add_argument('--input_vulnerability_curve', '-vc', type=str,
                        help='Input .csv file for a vulnerability curve.', required=True)
    parser.add_argument('--currency', '-c', type=str, default='£',
                        help='Currency for the vulnerability curve')
    parser.add_argument('--output_file', '-o', type=str, default='./damagecalc_results.csv',
                        help='Output file path for the damage cost results.')
    parser.add_argument('--log_verbosity', '-v', type=int, default=2,
                        help='Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.')
    args = parser.parse_args()

    # ? This will dump a log file wherever the user has navigated to.
    logging.basicConfig(filename='./damagecalc.log',
                        filemode='w', level=args.log_verbosity*10)

    for path in [args.input_depths, args.input_vulnerability_curve]:
        utils.check_file_exists(path)
        utils.check_is_file_csv(path)

    utils.check_is_file_csv(args.output_file)

    return args


def run_script(input_vulnerability_curve: str, input_depths: str, output_file: str, currency: str):
    '''Use this function if importing damagecalc for another script.'''

    vc = utils.vulnerability_curve(input_vulnerability_curve)
    total_cost, count, ignored = utils.calculate_damage_costs(
        input_depths, output_file, vc)

    print('''
    -----------------------------
    Total Cost: {}{:,.2f}
    Depth Values Processed: {}
    Skipped Values: {} (This should always be zero)
    -----------------------------
    '''.format(currency, total_cost, count, ignored))


def main():
    '''Entry point for the damage calculator script.'''
    try:
        args = get_arguments()
        run_script(args.input_vulnerability_curve,
                   args.input_depths, args.output_file, args.currency)
    except Exception as e:
        exception_string = str(e)
        print(exception_string)
        logging.fatal(exception_string)


if __name__ == "__main__":
    main()
