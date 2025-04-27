import pandas as pd

from app.io import DATA_DIR_PATH

PANDAS_FILENAME = 'color_srgb.csv'
VANILLA_READ_FILENAME = 'input.txt'

def input_from_console():
    """
    Function to input text from the console.

    Returns:
        str: Text entered by the user from the console
    """
    text = input("Enter some text > ")
    return text


def input_from_file_vanilla():
    """
    Function to read text from a file using built-in Python functionality.

    Returns:
        str: Text read from the file
    """
    try:
        with open(DATA_DIR_PATH + VANILLA_READ_FILENAME, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{VANILLA_READ_FILENAME}' not found."
    except Exception as e:
        return f"Error reading file: {e}"


def input_from_file_pandas():
    """
    Function to read a csv file using pandas library.

    Returns:
        str: String representation of the data read from the file
    """

    try:
        if PANDAS_FILENAME.endswith('.csv'):
            df = pd.read_csv(DATA_DIR_PATH + PANDAS_FILENAME)
        else:
           return f"Error reading file with pandas. Not a csv file: {PANDAS_FILENAME}"

        return str(df)
    except Exception as e:
        return f"Error reading file with pandas: {e}"