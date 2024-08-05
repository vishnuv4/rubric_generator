# Rubric Generator

This is a python script that automates the process of creating and updating assignment rubrics.

## Setup

Requires Python 3.12

Run the setup.ps1 script. All it does is create a virtual environment and install the tabulate package.

## Usage

To create a new template, update the assignment name and parameters in the rubric_generator.py script. Then run the script using python. 

If using VSCode, set the python interpreter to the venv created during the setup stage.

This will create a folder with the assignment name with a .py file of the same name as the assignment. Points for each question can be changed in the Rubric section.

Running this generated and then modified file will print the rubric on the console window and create an excel table so it can be easily copy-pasted.
