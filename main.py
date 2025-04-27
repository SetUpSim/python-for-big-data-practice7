from app.io.input import *
from app.io.output import *

def main():
    console_input = input_from_console()
    file_input_vanilla = input_from_file_vanilla()
    file_input_pandas = input_from_file_pandas()

    # Combine all results
    all_results = f"""
Results from different input methods:
-----------------------------------
From console input:\n{console_input}
-----------------------------------
From file input (vanilla Python):\n{file_input_vanilla}
-----------------------------------
From file input (pandas):\n{file_input_pandas}
-----------------------------------
"""

    output_to_console(all_results)

    result_message = output_to_file(all_results)
    output_to_console(result_message)

if __name__ == "__main__":
    main()