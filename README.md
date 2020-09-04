# Python Developer Coding Challenge
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
(env)  ~/ damagecalc --help
usage: damagecalc [-h] [--log_verbosity LOG_VERBOSITY]

Tool for calculating the expected £'s of damage for a quantifiable level of flood risk.

optional arguments:
  -h, --help            show this help message and exit
  --log_verbosity LOG_VERBOSITY, -v LOG_VERBOSITY
                        Logging verbosity (1 to 5) - level 1 is most verbose, level 5 logs critical entries only.
```