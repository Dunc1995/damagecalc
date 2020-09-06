import csv
import logging
import damagecalc as dc

def calculate_damage_costs(file_path: str, input_function, newline='', starting_index=1):
    '''Reads data rows in a .csv file and calls input_function() for every row. The output values can be found in damagecalc_results.csv'''
    cost_output = 0
    count = 0

    with open(dc.OUTPUT_FILE, 'w', newline='') as fo:
        fieldnames = ['depth', 'damage_cost']
        writer = csv.DictWriter(fo, fieldnames=fieldnames)
        writer.writeheader()

        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            for row in list(reader)[starting_index:]:
                result = input_function(row[0])
                writer.writerow({ 'depth': row[0], 'damage_cost': result })
                cost_output += result
                count += 1
    
    return cost_output, count

def get_list_from_csv(file_path: str, newline='', starting_index=1):
    '''Reads a csv file and returns its contents as a list object.'''
    output = []

    try:
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            for row in list(reader)[starting_index:]: #? Starting index omits the headings from the csv
                output.append(row)
    except Exception as e:
        output = None
        logging.fatal('Unable to read {}: {}'.format(file_path, str(e)))

    return output
    
