from custom_exceptions import FileProcessingError
from file_handler import FileHandler


def read_file(file_path):
    try:
        with FileHandler(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileProcessingError(f"The file at '{file_path}' was not found.")
    except IOError:
        raise FileProcessingError(f"An I/O error occurred while accessing the file at '{file_path}'.")
    finally:
        print("Finished attempting to read the file.")


def write_file(file_path, content):
    try:
        with FileHandler(file_path, 'w') as file:
            file.write(content)
    except PermissionError:
        raise FileProcessingError(f"Permission denied while writing to the file at '{file_path}'.")
    except IOError:
        raise FileProcessingError(f"An I/O error occurred while writing to the file at '{file_path}'.")
    else:
        print("File written successfully.")
    finally:
        print("Finished attempting to write to the file.")
