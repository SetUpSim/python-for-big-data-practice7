from app.io import DATA_DIR_PATH

OUTPUT_FILENAME = 'output.txt'

def output_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): Text to be displayed on the console
    """
    print(text)


def output_to_file(text):
    """
    Function to write text to a file using built-in Python functionality.

    Args:
        text (str): Text to be written to the file

    Returns:
        str: Message indicating success or failure
    """
    try:
        with open(DATA_DIR_PATH + OUTPUT_FILENAME, 'w', encoding='utf-8') as file:
            file.write(text)
        return f"Successfully wrote text to {OUTPUT_FILENAME}"
    except Exception as e:
        return f"Error writing to file: {e}"