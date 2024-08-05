# Rubric Generator

This is a python script that automates the process of creating and updating assignment rubrics.

## Setup

Requires Python 3.12

Run the setup.ps1 script. All it does is create a virtual environment and install the tabulate package.

## Usage

To create a new template, update the file name and assignment parameters in the rubric_generator.py script. Then run the script using python. 

If using VSCode, set the python interpreter to the venv created during the setup stage.

That should create a file with the desired name and parameters. Then when you run the file you will see the rubric in a tabular format.