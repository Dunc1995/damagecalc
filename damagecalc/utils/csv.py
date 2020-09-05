import csv

def get_dict_from_csv(file_path: str, newline=''):
    '''Reads a csv file and returns its contents as dict object.'''
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            