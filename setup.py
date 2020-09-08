from setuptools import setup, find_packages

setup(
    # Application name:
    name="Flood_Damage_Calculator",

    # Version number (initial):
    version="1.0.0",

    # Application author details:
    author="Duncan Bailey",
    author_email="duncanbailey1995@gmail.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/Dunc1995/damagecalc",

    #
    license="LICENSE",
    description="Coding challenge for a Python Developer job application.",
    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    # install_requires=[ ],

    entry_points={
        'console_scripts': [
            'damagecalc = damagecalc.__main__:main'
        ]
    }
)
