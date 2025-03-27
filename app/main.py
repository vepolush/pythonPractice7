from app.io.input import input_text_from_console, read_file, read_file_pandas

def main():
    text_from_console = input_text_from_console()
    print("Text from condole:")
    print(text_from_console)

    text_from_file = read_file('../data/letter')
    print("\nText from file:")
    print(text_from_file)

    text_from_file_pandas = read_file_pandas('../data/zoo.csv')
    print("Data frame from file using pandas:")
    print(text_from_file_pandas)

    with open('../data/main', "a") as file:
        file.write(text_from_console)
        file.write("\n")
        file.write("\n")
        file.write(text_from_file)
        file.write("\n")
        file.write(str(text_from_file_pandas))


if __name__ == "__main__":
    main()