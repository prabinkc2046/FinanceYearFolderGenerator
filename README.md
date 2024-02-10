# Business Problem

## Challenge:

You're tasked with creating a Python script that organizes financial data into folders based on fiscal years and months. Each folder represents a fiscal year, and within each fiscal year folder, there are subfolders representing each month of the fiscal year. However, there are certain constraints to be aware of:

The fiscal year starts from April and ends in March of the following year.
The script should prompt the user to input the start and end years for the data organization.
The script should ask the user to specify the name of the parent directory where all the fiscal year folders will be stored.
Each month subfolder should be named with the format "MM - Month YYYY", where MM is the month number (padded with a zero if less than 10) and YYYY is the year.
The script should handle existing folders gracefully, skipping their creation if they already exist.
Ensure that the script accounts for leap years correctly.

# Solution
Link to demo video [Automation script demonstration video](https://youtu.be/vrG-Jj0J5Ks)
## Finance Year Folder Generator

This Python script (`generate_folder_subfolder_bydate.py`) is designed to generate a folder structure corresponding to financial years, with subfolders representing each month within the financial year.

## How to Use

1. **Run the Script**: Execute the Python script `generate_folder_subfolder_bydate.py` in your terminal or Python environment.

```bash
python3 generate_folder_subfolder_bydate.py
```

2. **Input Start and End Years**: The script will prompt you to input the start, end years and directory for which you want to generate the folder structure. Enter the start and end years in the format `yyyy` (e.g., `2021`).

3. **Generated Folders**: The script will create a folder structure within the provided  directory. Each top-level folder represents a financial year (e.g., `2021-2022`). Within each financial year folder, subfolders are created to represent each month (e.g., `1-April 2021`, `2-May 2021`, ... `12-March 2022`).

