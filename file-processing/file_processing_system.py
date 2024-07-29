from file_operations import read_file, write_file
from custom_exceptions import FileProcessingError


def file_processing_system():
    content = None
    file_path = input("Enter the file path: ")
    operation = input("Enter the operation (read/write): ").strip().lower()

    if operation == "write":
        content = input("Enter the content to write to the file: ")

    try:
        if operation == "read":
            content = read_file(file_path)
            print("File content:")
            print(content)
        elif operation == "write":
            write_file(file_path, content)
            print("File written successfully.")
        else:
            print("Invalid operation. Please enter 'read' or 'write'.")
    except FileProcessingError as e:
        print(f"FileProcessingError: {e.message}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    file_processing_system()
