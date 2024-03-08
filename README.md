# Office File Organizer

---

The Office File Organizer is a Python script designed to efficiently organize various types of office files within a specified directory. It simplifies the process of file management by automatically categorizing files based on their types and moving them to their respective folders.

## Key Features

- **Smart File Classification:** The program intelligently identifies and classifies files into different categories based on their extensions. Supported file types include:
    - Documents: .doc, .docx, .txt
    - Spreadsheets: .xls, .xlsx
    - Presentations: .ppt, .pptx
    - PDFs: .pdf
    - Images: .jpg, .jpeg, .png, .gif
    - Audio: .mp3, .wav
    - Video: .mp4, .avi
    - Programming: .py, .html, .css, .js, .php, .java, .cpp, .c, .h, .cs, .rb, .pl, .sh, .sql, .csv
    - Others: .zip, .rar, .7z, .tar.gz, .tgz, .stl, .dwg, .skp, .blend, .svg, .psd, .ai, .epub, .mobi, .cbz, .cbr, .db, .sqlite, .mdb

- **Automated Organization:** Once files are classified, the program automatically creates folders for each category within the specified directory and moves the files accordingly.

- **Detailed Logging:** The program generates a detailed log of all operations performed during the file organization process. This log provides insights into which files were moved and where, facilitating easy tracking and verification.

---

## Usage

1. **Clone the Repository:** Download or clone the repository to your local machine.

2. **Install Dependencies:** Before running the program, you need to install the required Python dependencies. Open a terminal or command prompt, navigate to the directory where you downloaded/cloned the repository, and run the following command:
    ```bash
    pip install -r requirements.txt
    ```

    This command will automatically install all the necessary dependencies for the program to run smoothly.

3. **Run the Program:**

    - **Windows:** Open a terminal in the project directory and execute:
        ```cmd
        python office_file_organizer.py
        ```

    - **Linux:** Open a terminal in the project directory and execute:
        ```bash
        python3 office_file_organizer.py
        ```

4. **Follow the Instructions:** The program will display a menu with options to enter the directory path, view a description and help, execute the file organization, or exit the program.

---

## Supported Platforms

The Office File Organizer is compatible with Windows and Linux operating systems.

## System Requirements

- Python 3.x

- Python Dependencies (automatically installed from `requirements.txt`)

---

## License

© 2024 NurSoftware. All rights reserved.
# Office-File-Organizer
