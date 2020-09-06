# damagecalc
## Installation
Navigate to this repos directory and run the following command:
```
python setup.py install
```
> N.B. alternatively if you wish to test this script in isolation, you can execute the following to create a virtual environment:
>``` 
> python3 -m venv env;
> source env/bin/activate;
> python setup.py install;
>```
## Usage
After installation, you should be able to run the script like any normal CLI tool:
```
~/repos/damagecalc damagecalc --help
usage: damagecalc [-h] --input_depths INPUT_DEPTHS --input_vulnerability_curve INPUT_VULNERABILITY_CURVE [--currency CURRENCY] [--output_file OUTPUT_FILE]
                  [--log_verbosity LOG_VERBOSITY]

Tool for calculating the expected £'s of damage for a quantifiable level of flood risk.

optional arguments:
  -h, --help            show this help message and exit
  --input_depths INPUT_DEPTHS, -d INPUT_DEPTHS
                        Input .csv file for depth data.
  --input_vulnerability_curve INPUT_VULNERABILITY_CURVE, -vc INPUT_VULNERABILITY_CURVE
                        Input .csv file for a vulnerability curve.
  --currency CURRENCY, -c CURRENCY
                        Currency for the vulnerability curve
  --output_file OUTPUT_FILE, -o OUTPUT_FILE
                        Output file path for the damage cost results.
  --log_verbosity LOG_VERBOSITY, -v LOG_VERBOSITY
                        Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.
```