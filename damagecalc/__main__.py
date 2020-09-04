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

if __name__ == "__main__":
    main()