"""
Load text file data as a list of strings

Arguments:
    - text-file name and path if needed

Exceptions:
    - IOError if filename is not found

Requires - import sys
"""

import sys

def load(file):
    """
    Open a txt file and read lowercase strings to a list
    
    Returns:
        - A list of strings
    """
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError opening {file}", file=sys.stderr)
        sys.exit(1)