def read_file(file_path, encoding=None):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()#.strip()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None