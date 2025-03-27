import pandas as pd


def input_text_from_console():
    """
    Inputs text from console.

    Args:
        None

    Returns:
        str: User's entered text.

    Raises:
        None
    """
    user_input = input("Enter the text: ")
    return user_input


def read_file(file_path):
    """
    Reads file using python's built-in capabilities.

    Args:
        file_path: The path to the file to be read

    Returns:
        str: The text from the file.

    Raises:
        FileNotFoundError: if the file is not found.
    """
    with open(file_path) as file:
        file_content = file.read()
        return file_content

def read_file_pandas(file_path):
    """
    Reads file using pandas' built-in capabilities.

    Args:
        file_path: The path to the file to be read

    Returns:
        data frame: data frame from the file zoo.csv

    Raises:
        FileNotFoundError: if the file is not found.
    """
    df = pd.read_csv(file_path)
    return df
