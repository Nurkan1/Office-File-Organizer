import os
import shutil
from colorama import init, Fore
from tabulate import tabulate

# Initialize colorama to enable colors in the console
init(autoreset=True)

# Function to display the copyright message and a separator line
def show_header():
    """
    Displays the copyright message and a separator line.
    """
    print(Fore.YELLOW + "=" * 50)
    print(Fore.YELLOW + "© 2024 NurSoftware. All rights reserved.")
    print(Fore.YELLOW + "=" * 50)

def menu():
    """
    Displays the options menu.
    """
    print("\n" + Fore.CYAN + "Welcome to the Office File Organizer")
    print("1. Enter directory path")
    print("2. View description and help")
    print("3. Execute file organization")
    print("4. Exit")

def organize_files(directory):
    try:
        if not os.path.isabs(directory):
            directory = os.path.abspath(directory)
        print(Fore.GREEN + f"Organizing files in: {directory}")

        file_types = {
            'Documents': ['.doc', '.docx', '.txt'],
            'Spreadsheets': ['.xls', '.xlsx'],
            'Presentations': ['.ppt', '.pptx'],
            'PDFs': ['.pdf'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Audio': ['.mp3', '.wav'],
            'Video': ['.mp4', '.avi'],
            'Programming': ['.py', '.html', '.csv', '.css', '.js', '.php', '.java', '.cpp', '.c', '.h', '.cs', '.rb', '.pl', '.sh', '.sql'],
            'Others': ['.zip', '.rar', '.7z', '.tar.gz', '.tgz', '.stl', '.dwg', '.skp', '.blend', '.svg', '.psd', '.ai', '.epub', '.mobi', '.cbz', '.cbr', '.db', '.sqlite', '.mdb']
        }

        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                _, extension = os.path.splitext(file)
                file_moved = False
                for type, extensions in file_types.items():
                    if extension.lower() in extensions:
                        type_folder = os.path.join(directory, type)
                        if not os.path.exists(type_folder):
                            os.makedirs(type_folder, exist_ok=True)
                        destination = os.path.join(type_folder, file)
                        if file_path != destination:
                            try:
                                shutil.move(file_path, destination)
                                print(Fore.GREEN + f"{file} moved to {type}")
                                file_moved = True
                            except Exception as e:
                                print(Fore.RED + f"Error moving {file} to {type}: {e}")
                            break
                if not file_moved:
                    print(Fore.RED + f"{file} was not moved. It might already be in the correct folder or its type is not defined.")
    except FileNotFoundError:
        print(Fore.RED + f"Error: The specified directory does not exist: {directory}")

def main():
    """
    Main function of the program.
    """
    show_header()
    while True:
        menu()
        option = input(Fore.GREEN + "Select an option: ")
        if option == '1':
            directory = input(Fore.CYAN + "Enter the directory path: ")
            try:
                if os.path.isdir(directory):
                    organize_files(directory)
                    print(Fore.GREEN + "Files organized successfully.")
                else:
                    print(Fore.RED + "Error! Directory not found.")
            except Exception as e:
                print(Fore.RED + f"An unexpected error occurred: {e}")
        elif option == '2':
            print(Fore.CYAN + "Program description:\n" +
            "This innovative script turns chaos into order by meticulously organizing your\n" +
            "office files by type in the directory of your choice. Designed to maximize\n" +
            "efficiency and simplify document searching, this tool is indispensable for any\n" +
            "digital professional.\n\n" +
            "Key features:\n" +
            "- Smart classification: Identifies and classifies files by type, including\n" +
            "  documents, spreadsheets, presentations, PDFs, images, audio and\n" +
            "  video files, ensuring each file is stored in its designated folder.\n" +
            "- Automated organization: With just a few clicks, moves files to their\n" +
            "  corresponding folders, eliminating the need for manual sorting and saving\n" +
            "  countless hours.\n" +
            "- Detailed logging: For flawless tracking, automatically generates a log\n" +
            "  of all performed operations, allowing you to review and verify file\n" +
            "  organization.\n\n" +
            "Use this script to say goodbye to disorder and welcome a more organized and\n" +
            "productive digital workspace.")
        elif option == '3':
            if 'directory' in locals():
                organize_files(directory)
                print(Fore.GREEN + "Files organized successfully.")
            else:
                print(Fore.RED + "Error! You must first enter the directory path.")
        elif option == '4':
            print(Fore.YELLOW + "See you later!")
            break
        else:
            print(Fore.RED + "Invalid option!")

if __name__ == "__main__":
    main()
