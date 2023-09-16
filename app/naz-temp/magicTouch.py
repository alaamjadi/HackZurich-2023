import magic

def get_file_type(file_path):
    # Create a magic object
    magic_obj = magic.Magic()

    # Use the magic object to identify the file type
    file_type = magic_obj.from_file(file_path)

    return file_type

# Example usage:
file_path = "path/to/your/file.ext"
file_type = get_file_type(file_path)
print(f"The file {file_path} is of type: {file_type}")
