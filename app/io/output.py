def output_text_to_console(text):
    """
    Outputs text to the console.

    Args:
        text (str): The text to be printed to the console.

    Returns:
        None
    """
    print(text)


def write_to_the_file(file_path, text):
    """
    Writes text to the file.

    Args:
        file_path: The path of the file to write to.
        text (str): The text to be written.

    Returns:
        None

    Raises:
        FileNotFoundError: if the file is not found.
    """
    with open(file_path, "w") as file:
        file.write(text)
