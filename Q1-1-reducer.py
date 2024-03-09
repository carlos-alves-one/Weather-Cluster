
#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Reducer for Question No.1 Task 1:
#
# The reducer aggregates wind speeds by date, ignoring the WBAN Number. It calculates
# the difference between the maximum and minimum wind speeds for each date.

# Importing necessary libraries
import sys

# Global variables
current_date = None
max_wind_speed = 0
min_wind_speed = float('inf')

# Function to reset min and max for a new date
def reset_min_max():

    # Reset global variables
    global max_wind_speed, min_wind_speed
    max_wind_speed = 0
    min_wind_speed = float('inf')

# Emit the results for the current date
def emit_results(date):

    # Emit the results if the date is not None and the max and min wind speeds are valid
    global max_wind_speed, min_wind_speed
    if date and (max_wind_speed is not None and min_wind_speed is not float('inf')):
        print(f"{date}\t{max_wind_speed - min_wind_speed}")

        # Reset min and max for the next date
        reset_min_max()

# Reducer function to process each line of input
def reducer():

    # Reading input from standard input
    global current_date, max_wind_speed, min_wind_speed

    # Processing each line of input
    for line in sys.stdin:

        # Splitting the input to extract date and wind speed, ignoring WBAN Number
        composite_key, value = line.strip().split('\t')
        _, date = composite_key.split('-', 1)  # Splitting composite key and taking date part
        wind_speed = float(value)

        # If the date is different from the current date, emit the results for the current date
        if date != current_date:

            # Emit results for the previous date
            emit_results(current_date)

            # Update the current date
            current_date = date
        
        # Update the max and min wind speeds
        max_wind_speed = max(max_wind_speed, wind_speed)
        min_wind_speed = min(min_wind_speed, wind_speed)

    # Emit results for the last date
    emit_results(current_date)

# Calling the reducer function
if __name__ == "__main__":
    reducer()
