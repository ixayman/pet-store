from contextlib import contextmanager
from custom_exceptions import FileProcessingError


@contextmanager
def FileHandler(file_path, mode):
    file = None
    try:
        file = open(file_path, mode)
        yield file
    except Exception as e:
        raise FileProcessingError(f"An error occurred: {e}")
    finally:
        if file:
            file.close()
            print("File closed.")
