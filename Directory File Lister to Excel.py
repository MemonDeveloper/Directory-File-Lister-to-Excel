import os
from openpyxl import Workbook

# Define allowed document file extensions
ALLOWED_EXTENSIONS = {'.xlsm', '.csv', '.txt', '.jpg'}

def listdir_to_excel(dir, output_file):
    wb = Workbook()
    ws = wb.active

    file_paths = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ALLOWED_EXTENSIONS:
                file_paths.append(os.path.join(root, file))

    total = len(file_paths)
    print(f"Total matching files found: {total}")

    max_depth = 0
    relative_paths = []

    for path in file_paths:
        relative = os.path.relpath(path, dir)
        parts = relative.split(os.path.sep)
        relative_paths.append(parts)
        if len(parts) > max_depth:
            max_depth = len(parts)

    header = [f"Level {i+1}" for i in range(max_depth-1)] + ["FileName"]
    ws.append(header)

    for i, parts in enumerate(relative_paths):
        row = parts[:-1] + [""] * (max_depth - 1 - len(parts[:-1])) + [parts[-1]]
        ws.append(row)
        percent = ((i + 1) / total) * 100
        print(f"Processing: {percent:.2f}% complete", end='\r')

    wb.save(output_file)
    print(f"\nFile paths written to {output_file}")

if __name__ == '__main__':
    folderpath = input("Enter the folder path: ").strip()
    if not os.path.isdir(folderpath):
        print("Invalid folder path.")
    else:
        output_file = os.path.join(folderpath, "documentfilelist.xlsx")
        listdir_to_excel(folderpath, output_file)