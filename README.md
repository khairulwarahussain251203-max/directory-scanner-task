# Directory Scanner

A Python tool that scans a given folder (including all subfolders) and generates
a report listing every file and folder found, along with each file's size,
extension, and last modified date. Results are saved to a `.txt` file.

## Concepts Covered
- Python fundamentals (loops, conditionals, exception handling, f-strings)
- Object-Oriented Programming (a `DirectoryScanner` class with methods and static helpers)
- File Handling (`os.walk`, `os.path.getsize`, `os.path.getmtime`, writing to `.txt`)

## How to Run
\`\`\`bash
python3 directory_scanner.py
\`\`\`
You'll be prompted to enter a folder path to scan (press Enter to scan the current folder).

## Output
A `scan_report.txt` file is generated containing:
- Every folder and file found
- File size (human-readable: B/KB/MB/GB)
- File extension
- Last modified date/time
- A summary (total folders, total files, total size)