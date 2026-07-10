"""
Directory Scanner
-----------------
Internship Task: Python Fundamentals + OOP + File Handling

What it does:
1. Scans a given folder (recursively, including subfolders).
2. Lists all files and subfolders found.
3. For each file, shows: size, extension, and last modified date.
4. Saves the full report into a .txt file.

Concepts used:
- OOP        : A DirectoryScanner class encapsulates all the scanning logic.
- File I/O   : Reading directory contents, writing the report to a .txt file.
- Python fundamentals : loops, conditionals, string formatting, exception handling,
                         f-strings, list/tuple usage, functions/methods.
"""

import os
from datetime import datetime


class DirectoryScanner:
    """
    A simple, reusable directory scanner.

    Usage:
        scanner = DirectoryScanner(target_path="some/folder", output_file="report.txt")
        scanner.scan()
        scanner.save_report()
    """

    def __init__(self, target_path: str, output_file: str = "scan_report.txt"):
        self.target_path = target_path
        self.output_file = output_file
        self.report_lines = []   # holds every line we will eventually write to the txt file
        self.total_files = 0
        self.total_folders = 0
        self.total_size_bytes = 0

    # ---------- Helper methods ----------

    @staticmethod
    def format_size(size_in_bytes: int) -> str:
        """Convert raw byte count into a human-readable string (KB, MB, GB)."""
        size = float(size_in_bytes)
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"

    @staticmethod
    def get_last_modified(path: str) -> str:
        """Return a readable last-modified timestamp for a given path."""
        timestamp = os.path.getmtime(path)
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    def _log(self, line: str = ""):
        """Add a line to the in-memory report and print it to the console."""
        print(line)
        self.report_lines.append(line)

    # ---------- Core scanning logic ----------

    def scan(self):
        """Walk through the target directory and build the report."""
        if not os.path.exists(self.target_path):
            raise FileNotFoundError(f"The path '{self.target_path}' does not exist.")

        self._log(f"Directory Scan Report")
        self._log(f"Target Path : {os.path.abspath(self.target_path)}")
        self._log(f"Scanned On  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self._log("=" * 70)

        # os.walk gives us (current_folder, list_of_subfolders, list_of_files)
        for root, dirs, files in os.walk(self.target_path):
            self._log(f"\n[FOLDER] {root}")
            self.total_folders += len(dirs)

            if not files and not dirs:
                self._log("   (empty folder)")

            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    size_bytes = os.path.getsize(file_path)
                    extension = os.path.splitext(file_name)[1] or "(no extension)"
                    last_modified = self.get_last_modified(file_path)

                    self._log(
                        f"   [FILE] {file_name:<35} "
                        f"| Size: {self.format_size(size_bytes):<10} "
                        f"| Ext: {extension:<10} "
                        f"| Modified: {last_modified}"
                    )

                    self.total_files += 1
                    self.total_size_bytes += size_bytes

                except OSError as e:
                    # Handles edge cases like permission errors or broken symlinks
                    self._log(f"   [ERROR] Could not read '{file_name}': {e}")

        self._log("\n" + "=" * 70)
        self._log("SUMMARY")
        self._log(f"Total Folders Scanned : {self.total_folders}")
        self._log(f"Total Files Found     : {self.total_files}")
        self._log(f"Total Size            : {self.format_size(self.total_size_bytes)}")

    def save_report(self):
        """Write the collected report lines into the output .txt file."""
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(self.report_lines))
        print(f"\nReport saved to: {os.path.abspath(self.output_file)}")


def main():
    # Change this path to whatever folder you want to scan.
    # "." means "the current folder this script is run from".
    target_folder = input("Enter folder path to scan (or press Enter for current folder): ").strip()
    if not target_folder:
        target_folder = "."

    output_txt = "scan_report.txt"

    scanner = DirectoryScanner(target_path=target_folder, output_file=output_txt)

    try:
        scanner.scan()
        scanner.save_report()
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()