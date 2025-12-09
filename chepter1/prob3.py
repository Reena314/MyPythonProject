import os

def print_directory_contents(path='/Born to learn'):
    """
    Print the names of entries (files, directories) in the given directory path.
    If no path is given, uses the current directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: Directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")
        return

    for entry in entries:
        print(entry)

if __name__ == "__main__":
    # You can change this to any directory you want
    directory_to_list = input("Enter directory path (or leave blank for current): ").strip()
    if directory_to_list == "":
        directory_to_list = "."
    print(f"Contents of '{directory_to_list}':")
    print_directory_contents(directory_to_list)
