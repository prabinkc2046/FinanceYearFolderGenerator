import os

# Function to generate year ranges
def generate_year_range(start, end):
    # Initialize an empty list to store the generated year ranges
    year_ranges = []
    
    # Iterate through the range of years from the start to the end year (exclusive)
    for year in range(start, end):
        # Generate a year range string (e.g., "2021-2022") and append it to the list
        year_range = f"{year}-{year+1}"
        year_ranges.append(year_range)
    
    # Print the generated year ranges for reference
    print(f"Following year ranges will be used to generate folders: {year_ranges}")
    
    # Return the list of generated year ranges
    return year_ranges

# Function to generate date ranges for each year range
def generate_date_range(year_range):
    # Split the year range string into start year and end year
    start_year, end_year = map(int, year_range.split('-'))
    
    # Initialize an empty list to store the generated date ranges
    dates_in_range = []
    
    # Define the names of months in a financial year starting from April to March
    month_names = ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March']
    
    # Initialize a counter to track the index of each month
    counter = 1
    
    # Iterate through the years within the given year range
    for year in range(start_year, end_year):
        # Iterate through the month names
        for month_index, month_name in enumerate(month_names):
            # Generate a formatted date string for each month
            if month_index <= 8:
                if counter < 10:
                    date_string = f"{0}{counter} - {month_name} {year}"
                    dates_in_range.append(date_string)
                    counter += 1
            if month_index > 8:
                date_string = f"{counter} - {month_name} {year+1}"
                dates_in_range.append(date_string)
                counter += 1
    
    # Return the list of generated date ranges
    return dates_in_range

# Get start year and end year from the user
start_year = int(input("Type start year please (format yyyy): "))
end_year = int(input("Type end year (format yyyy): "))
parent_directory = input("Name your parent directory: ")
# Generate year ranges
year_ranges = generate_year_range(start_year, end_year)

# Iterate through each generated year range
for year_range in year_ranges:
    # Define the parent directory where folders will be created for the current year range
    parent_directory = "./" + parent_directory
    folder_path = os.path.join(parent_directory, year_range)
    
    # Create parent directory if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{year_range}' created at path '{folder_path}'")
    else:
        print(f"Folder '{year_range}' already exists at path '{folder_path}'. Skipping creation.")
    
    #Generate date range for the current year range
    date_range = generate_date_range(year_range)
    
    # Iterate through each generated date in the date range
    for date in date_range:
        # Define the child folder path within the parent directory
        child_folder_path = os.path.join(folder_path, date)
        
        # Create subfolder if it doesn't exist
        if not os.path.exists(child_folder_path):
            os.makedirs(child_folder_path)
            print(f"Subfolder '{date}' created at path '{child_folder_path}'")
        else:
            print(f"Subfolder '{date}' already exists at path '{child_folder_path}'. Skipping creation.")
