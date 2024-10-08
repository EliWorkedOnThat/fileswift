#!/usr/bin/env python3

import os
import shutil
import difflib
import filecmp


def help():
    page = input("Please choose help line (1) Command line help (2) Creator message: ")
    if page == "1":
        print("The help menu provides a simple guide on what FileSwift can do:")
        print("1# = Make a new directory at a location specified by the user.")
        print("2# = Delete a directory, listing all directories dynamically (only empty directories).")
        print("3# = Reroute the user to a specified PATH.")
        print("4# = Get information on a directory/file.")
        print("5# = Rename a directory/file specified by the user.")
        print("6# = Check if a PATH exists.")
        print("7# = Create a new file.")
        print("8# = Delete a file.")
        print("9# = Delete a directory and all its contents recursively.")
        print("10# = Delete all files in a directory and its subdirectories recursively.")
        print("11# = Move directories or files / Change PATH/Location of Files and Directories")
        print("12# = Compare file/directories by providing PATH for both and gather information about them")
        print("13# = Search for file/directory by name or starting PATH.")
    elif page == "2":
        print("FileSwift was designed to help new Linux users or anyone who finds directory management challenging.")
        print("This tool simplifies command-line navigation, with commands laid out in a clear menu format.")
        print("It's designed by a 17-year-old who loves coding and wants to help others! Feedback appreciated via email: ")


# Function to make a new directory at any specified location
def make_new_directory():
    new_directory_name = input("What do you want the new directory name to be? ").strip()
    path_to_create = input("Where do you want to create this directory? (Leave blank for Desktop): ").strip()

    if not new_directory_name:
        print("Directory name cannot be empty.")
        return

    if not path_to_create:
        path_to_create = os.path.join(os.path.expanduser("~"), "Desktop")

    new_dir_path = os.path.join(path_to_create, new_directory_name)

    try:
        os.mkdir(new_dir_path)
        print(f"Directory '{new_directory_name}' created successfully at '{path_to_create}'!")
    except FileExistsError:
        print(f"Directory '{new_directory_name}' already exists at '{path_to_create}'.")
    except OSError as error:
        print(f"Error creating directory: {error}")

# Function to delete a directory at any specified location
def delete_directory():
    print("Please make sure that you dont accidentally delete a directory you may need double check PATH to make sure not to delete anything valuable")
    safety_check = input("Do you wish to continue: (1) Continue to deletion (2)Terminate Process ")
    if safety_check == "1":

        delete_from_path = input("Please provide the PATH where the directory is located (Leave blank for Desktop): ").strip()

        if not delete_from_path:
            delete_from_path = os.path.join(os.path.expanduser("~"), "Desktop")

        directories = [item for item in os.listdir(delete_from_path) if os.path.isdir(os.path.join(delete_from_path, item))]

        if not directories:
            print(f"No directories found at '{delete_from_path}'.")
            return

        print("Directories found:")
        for idx, dir_name in enumerate(directories, 1):
            print(f"{idx}. {dir_name}")

        try:
            choice = int(input("Please choose the directory you want to delete by number: ")) - 1
            if choice < 0 or choice >= len(directories):
                print("Invalid selection.")
                return

            dir_to_delete = directories[choice]
            dir_path_to_delete = os.path.join(delete_from_path, dir_to_delete)

            os.rmdir(dir_path_to_delete)
            print(f"Directory '{dir_to_delete}' deleted successfully from '{delete_from_path}'.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except FileNotFoundError:
            print(f"The directory was not found.")
        except OSError as error:
            print(f"Error: {error}. The directory might not be empty.")

    elif safety_check == "2":
            print("Process Stopped...")

# Function to reroute user to a specified path
def reroute():
    path_tgt = input("Please input the PATH to reroute to: ").strip()

    if not path_tgt:
        print("PATH cannot be empty.")
        return

    try:
        os.chdir(path_tgt)
        print(f"Successfully changed the directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"The specified path '{path_tgt}' does not exist.")
    except NotADirectoryError:
        print(f"The specified path '{path_tgt}' is not a directory.")
    except PermissionError:
        print(f"You do not have permission to access '{path_tgt}'.")
    except OSError as error:
        print(f"Error changing directory: {error}")

# Function to rename directories/files
def rename():
    src = input("Please provide the old name with its directory (Example: old_directory/old_file.txt): ").strip()
    dst = input("Please provide a new name (Example: new_directory/new_file.txt): ").strip()

    safety_check = input(
        "Renaming may change the location or PATH. Continue? (Y/N): "
    ).capitalize()

    if safety_check == "Y":
        if os.path.exists(src):
            try:
                os.rename(src, dst)
                print(f"Successfully renamed '{src}' to '{dst}'")
            except FileExistsError:
                print(f"Error: A file named '{dst}' already exists.")
            except PermissionError:
                print(f"Error: Permission denied. Cannot rename '{src}'.")
            except OSError as e:
                print(f"Error: {e}")
        else:
            print(f"Error: The file '{src}' does not exist.")
    elif safety_check == "N":
        print("Action Stopped!")
    else:
        print("Invalid input! Please enter 'Y' or 'N'.")

# Function to get information on a directory or file
def get_directory_info():
    path = input("Please provide the PATH for the directory/file to check: ").strip()

    if os.path.exists(path):
        stat_info = os.stat(path)
        print(f"Path: {path}")
        print(f"Size: {stat_info.st_size} bytes")
        print(f"Last modified: {stat_info.st_mtime}")
        print(f"Creation time: {stat_info.st_ctime}")
        print(f"Access time: {stat_info.st_atime}")
    else:
        print(f"The provided path '{path}' does not exist.")

def check_for_path():
    check_path = input("Please provide a PATH to check: ").strip()

    if os.path.exists(check_path):
        if os.path.isdir(check_path):
            print(f"The provided path exists and it's a directory.")
        elif os.path.isfile(check_path):
            print(f"The provided path exists and it's a file.")
    else:
        create_dir = input("The provided path does not exist. Create it? (Y/N): ").strip().capitalize()
        if create_dir == 'Y':
            try:
                os.mkdir(check_path)
                print(f"Directory '{check_path}' created successfully!")
            except OSError as error:
                print(f"Error creating directory: {error}")
        else:
            print("No changes made.")

# Function to create a new file in any specified location
def create_file():
    file_name = input("What do you want to name the new file (include extension)? ").strip()
    path_to_create = input("Where do you want to create this file? (Leave blank for Desktop or Home): ").strip()

    # Ensure the file name is provided
    if not file_name:
        print("File name cannot be empty.")
        return

    # If no path is provided, default to Desktop or Home directory
    if not path_to_create:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        if os.path.exists(desktop_path):
            path_to_create = desktop_path
        else:
            print("Desktop not found. Using Home directory.")
            path_to_create = os.path.expanduser("~")

    # Combine the path with the file name to get the full file path
    file_path = os.path.join(path_to_create, file_name)

    # Check if the file already exists
    if os.path.exists(file_path):
        overwrite = input(f"File '{file_name}' already exists. Overwrite? (Y/N): ").strip().capitalize()
        if overwrite != 'Y':
            print("File creation aborted.")
            return

    # Attempt to create the file
    try:
        with open(file_path, 'w') as file:
            print(f"File '{file_name}' created successfully at '{path_to_create}'!")
    except OSError as error:
        print(f"Error creating file: {error}")


# Function to delete a file
def delete_file():

    print("Please make sure that you dont accidentally delete a file you may need double check PATH to make sure not to delete anything valuable")
    safety_check = input("Do you wish to continue: (1) Continue to deletion (2)Terminate Process ")
    if safety_check == "1":
        delete_from_path = input("Please provide the PATH where the file is located (Leave blank for Desktop): ").strip()

        if not delete_from_path:
            delete_from_path = os.path.join(os.path.expanduser("~"), "Desktop")

        files = [item for item in os.listdir(delete_from_path) if os.path.isfile(os.path.join(delete_from_path, item))]

        if not files:
            print(f"No files found at '{delete_from_path}'.")
            return

        print("Files found:")
        for idx, file_name in enumerate(files, 1):
            print(f"{idx}. {file_name}")

        try:
            choice = int(input("Please choose the file you want to delete by number: ")) - 1
            if choice < 0 or choice >= len(files):
                print("Invalid selection.")
                return

            file_to_delete = files[choice]
            file_path_to_delete = os.path.join(delete_from_path, file_to_delete)

            os.remove(file_path_to_delete)
            print(f"File '{file_to_delete}' deleted successfully from '{delete_from_path}'.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except FileNotFoundError:
            print(f"The file was not found.")
        except OSError as error:
            print(f"Error: {error}")

    elif safety_check == "2":
        print("Process Stopped...")

def delete_directory_recursively():
    print(
        "Please make sure that you don't accidentally delete a directory you may need. Double-check the PATH to avoid deleting anything valuable.")
    safety_check = input("Do you wish to continue? (1) Continue to deletion (2) Terminate Process: ")

    if safety_check == "1":
        delete_from_path = input(
            "Please provide the PATH where the directory is located (Leave blank for Desktop): ").strip()

        if not delete_from_path:
            delete_from_path = os.path.join(os.path.expanduser("~"), "Desktop")

        directories = [item for item in os.listdir(delete_from_path) if
                       os.path.isdir(os.path.join(delete_from_path, item))]

        if not directories:
            print(f"No directories found at '{delete_from_path}'.")
            return

        print("Directories found:")
        for idx, dir_name in enumerate(directories, 1):
            print(f"{idx}. {dir_name}")

        try:
            choice = int(input("Please choose the directory you want to delete by number: ")) - 1
            if choice < 0 or choice >= len(directories):
                print("Invalid selection.")
                return

            dir_to_delete = directories[choice]
            dir_path_to_delete = os.path.join(delete_from_path, dir_to_delete)

            # Use shutil.rmtree to delete the directory and its contents recursively
            shutil.rmtree(dir_path_to_delete)
            print(
                f"Directory '{dir_to_delete}' and all its contents have been deleted successfully from '{delete_from_path}'.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except FileNotFoundError:
            print(f"The directory was not found.")
        except OSError as error:
            print(f"Error: {error}.")

    elif safety_check == "2":
        print("Process Stopped...")

def delete_files_recursively():
    print(
        "Please make sure that you don't accidentally delete files you may need. Double-check PATH to ensure you don't delete anything valuable."
        "Deleting files recursively will destroy all files in the PATH you specify !!!")
    safety_check = input("Do you wish to continue? (1) Continue to deletion (2) Terminate Process ")

    if safety_check == "1":
        delete_from_path = input(
            "Please provide the PATH where the files are located (Leave blank for Desktop): ").strip()

        if not delete_from_path:
            delete_from_path = os.path.join(os.path.expanduser("~"), "Desktop")

        if not os.path.exists(delete_from_path):
            print(f"The specified path '{delete_from_path}' does not exist.")
            return

        try:
            # Walk through the directory and delete files
            for root, dirs, files in os.walk(delete_from_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")

            print("All files deleted successfully from the specified directory and its subdirectories.")

        except Exception as e:
            print(f"An error occurred: {e}")

    elif safety_check == "2":
        print("Process Stopped...")


def move_file_or_directory(source, destination):
    try:
        # Check if the source exists
        if not os.path.exists(source):
            print(f"Error: The source '{source}' does not exist.")
            return

        # Check if the destination exists
        if not os.path.exists(destination):
            print(f"Error: The destination '{destination}' does not exist.")
            return

        # Move the file or directory
        shutil.move(source, destination)
        print(f"Successfully moved '{source}' to '{destination}'.")

    except Exception as e:
        print(f"Error: {e}")

#Function to compare a file or directory
def compare_file_directory():
    # Getting the paths from user input
    print("Please provide the first PATH of the file/directory you want to compare:")
    PATH_COMPARE_1 = input("PATH 1: ")
    print("Please provide the second PATH of the file/directory you want to compare:")
    PATH_COMPARE_2 = input("PATH 2: ")

    # Check if both paths are valid
    if not os.path.exists(PATH_COMPARE_1):
        print(f"Error: {PATH_COMPARE_1} does not exist.")
        return
    if not os.path.exists(PATH_COMPARE_2):
        print(f"Error: {PATH_COMPARE_2} does not exist.")
        return

    # Check if both are files
    if os.path.isfile(PATH_COMPARE_1) and os.path.isfile(PATH_COMPARE_2):
        print("Both paths are files. Comparing files...")
        compare_files(PATH_COMPARE_1, PATH_COMPARE_2)

    # Check if both are directories
    elif os.path.isdir(PATH_COMPARE_1) and os.path.isdir(PATH_COMPARE_2):
        print("Both paths are directories. Comparing directories...")
        compare_directories(PATH_COMPARE_1, PATH_COMPARE_2)

    else:
        print("Error: The provided paths do not match (one is a file and the other is a directory).")


def compare_files(file1, file2):
    """Compares two files line by line using difflib."""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    # Using difflib to compare the files
    d = difflib.Differ()
    diff = list(d.compare(f1_lines, f2_lines))

    # Output the differences
    print("\nDifferences between files:")
    for line in diff:
        print(line)


def compare_directories(dir1, dir2):
    """Compares two directories by comparing files in both directories."""
    comparison = filecmp.dircmp(dir1, dir2)

    # Output differences in directory structure
    print("\nFiles only in", dir1, ":", comparison.left_only)
    print("Files only in", dir2, ":", comparison.right_only)
    print("Common files:", comparison.common_files)

    # Compare contents of files that are common to both directories
    for file in comparison.common_files:
        file1 = os.path.join(dir1, file)
        file2 = os.path.join(dir2, file)

        print(f"\nComparing common file: {file}")
        compare_files(file1, file2)

#Function to find file/directory by name
def search():
    print("Please make sure the name of the file or directory is spelled correctly!")
    search_target = input("Enter the file/directory name: ").strip()

    if not search_target:
        print("Search target cannot be empty.")
        return

    # Ask the user if they want to specify a starting path
    choice2 = input("Do you want to specify a starting PATH? (Y/N): ").strip().capitalize()

    if choice2 == "Y":
        start_path = input("Provide a starting PATH: ").strip()
        if not start_path or not os.path.exists(start_path):
            print(f"The provided path '{start_path}' is invalid or does not exist.")
            return
    elif choice2 == "N":
        print("Searching in Home directory and generic system directories...")
        start_path = os.path.expanduser("~")  # Home directory

    # Search in Home and typical Linux directories
    directories_to_search = [
        start_path,
        "/etc",
        "/usr",
        "/var",
        "/opt",
        "/tmp",
        "/root",
        "/boot",
        "/sbin",
        "/lib",
        "/lib64",
        "/bin",
        "/mnt",
        "/media",
        "/srv",
        "/var/lib",
        "/home",
        "/proc",
        "/sys",
        "/run"
    ]

    found_items = []

    # Traverse through each directory
    for dir_to_search in directories_to_search:
        print(f"Searching in: {dir_to_search}")

        for root, dirs, files in os.walk(dir_to_search):
            # Check for matching directories
            for directory in dirs:
                if search_target.lower() in directory.lower():
                    found_items.append(os.path.join(root, directory))

            # Check for matching files
            for file in files:
                if search_target.lower() in file.lower():
                    found_items.append(os.path.join(root, file))

    # Display the search results
    if found_items:
        print("\nFound the following matches:")
        for item in found_items:
            print(item)
    else:
        print(f"No matches found for '{search_target}'.")

# Main function with user menu
def main():
    print("Welcome to FileSwift, a tool designed to simplify Linux directory management! (Use sudo in order to ensure all functionalities work correctly :D)")
    print()
    while True:
        userinput = input("Select a function:\n"
                          "1. Make New Directory\n"
                          "2. Delete Directory (simple/empty directory)\n"
                          "3. Reroute by PATH\n"
                          "4. Get directory/file info\n"
                          "5. Rename directory/file\n"
                          "6. Check if PATH exists\n"
                          "7. Create New File\n"
                          "8. Delete File\n"
                          "9. Help\n"
                          "10. Delete Directory (recursively)\n"
                          "11. Delete Files (recursively)\n"
                          "12. Move File or Directory\n"
                          "13. Compare File or Directory\n"
                          "14. Search\n"
                          "0. Exit\n"
                          "Enter your choice (0-13): ").strip()

        match userinput:
            case "1":
                make_new_directory()
            case "2":
                delete_directory()
            case "3":
                reroute()
            case "4":
                get_directory_info()
            case "5":
                rename()
            case "6":
                check_for_path()
            case "7":
                create_file()
            case "8":
                delete_file()
            case "9":
                help()
            case "10":
                delete_directory_recursively()
            case "11":
                delete_files_recursively()
            case "12":
                source = input("Enter the source path (file or directory): ")
                destination = input("Enter the destination path: ")
                move_file_or_directory(source, destination)
            case "13":
                compare_file_directory()
            case "14":
                search()
            case "0":
                print("Exiting program...")
                break
            case _:
                print("Invalid input. Please enter a number from 0 to 14.")

main()