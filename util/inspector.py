import os
import subprocess

from env import PJCT_PATH as project_dir

def analyze_code(dir):
    """
    This fcn checks all scripts in a directory 
    for bugs using pylint and flake8
    """
    # list Python files in the directory
    py_files = [file for file in os.listdir(dir) if file.endswith('.py')]

    if not py_files:
        print("No Python files found in the specified dir.")
        return

    # analyze each python file using pylint and flake8
    for file in py_files:
        print(f"Analyzing file: {file}")
        file_path = os.path.join(dir, file)

        print("\nRunning pylint...")
        pylint_command = f"pylint {file_path}"
        subprocess.run(pylint_command, shell=True)

        print("\nRunning flake8...")
        flake8_command = f"flake8 {file_path}"
        subprocess.run(flake8_command, shell=True)

if __name__ == "__main__":
    analyze_code(project_dir)