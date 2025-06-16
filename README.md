# Directory File Lister to Excel 📁📄

This Python script helps you easily list all files within a specified directory and its subdirectories, then export this organized list into an Excel workbook. It's particularly useful for documenting file structures or creating inventories of specific file types.

-----

## Features ✨

  * **Recursive Listing**: Traverses through all subdirectories to find files.
  * **Filtered by Extension**: Only lists files with specific, allowed extensions (e.g., `.xlsm`, `.csv`, `.txt`, `.jpg`). You can easily customize these extensions.
  * **Structured Output**: Organizes the file paths into an Excel sheet, breaking down the directory structure into separate columns for better readability.
  * **Progress Indicator**: Displays a real-time progress percentage during file processing.
  * **Automatic Naming**: Saves the output Excel file as `documentfilelist.xlsx` directly within the scanned folder.

-----

## Prerequisites 🛠️

Before running this script, ensure you have the following installed:

  * **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
  * **`openpyxl` library**: This is a Python library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.

-----

## Installation 💻

1.  **Clone the repository** (or download the `main.py` file):
    ```bash
    git clone https://github.com/MemonDeveloper/Directory-File-Lister-to-Excel.git
    cd Directory-File-Lister-to-Excel
    ```
2.  **Create a `requirements.txt` file**: In the root directory of your project, create a file named `requirements.txt` and paste the following content:
    ```
    openpyxl
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

-----

## Configuration ⚙️

You can easily modify the types of files the script will list. Open the `main.py` file and edit the `ALLOWED_EXTENSIONS` set:

```python
ALLOWED_EXTENSIONS = {'.xlsm', '.csv', '.txt', '.jpg'} # Add or remove extensions as needed
```

Remember to include the leading dot (`.`) for each extension.

-----

## Usage ▶️

1.  **Run the script**:

    ```bash
    python main.py
    ```

2.  **Enter the folder path**: The script will prompt you to enter the full path to the directory you want to scan:

    ```
    Enter the folder path: C:\Users\YourUser\Documents\MyProjectFiles
    ```

    (On Linux/macOS, it might look like `/home/youruser/my_project_files/`)

The script will then scan the specified folder and its subdirectories. Once completed, an Excel file named `documentfilelist.xlsx` will be created in the same folder you provided as input.

-----

## Output Excel Format 📊

The generated Excel file (`documentfilelist.xlsx`) will have columns representing the directory levels, followed by the filename. For example, if your folder structure is `FolderA/SubFolder1/file.txt`, the columns might look like:

| Level 1 | Level 2 | FileName |
| :------ | :------ | :------- |
| FolderA | SubFolder1 | file.txt |
| FolderA | SubFolder2 | another\_file.csv |
| ... | ... | ... |

-----

## Important Notes ⚠️

  * **Large Directories**: Processing very large directories with many files and deep nesting can take some time.
  * **Permissions**: Ensure the script has the necessary read permissions for the specified folder and write permissions to create the Excel file within that folder.

-----

## Contributing 🤝

Feel free to fork this repository, open issues, and submit pull requests if you have suggestions for improvements or bug fixes.

-----
