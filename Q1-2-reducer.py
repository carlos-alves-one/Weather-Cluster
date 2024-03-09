
#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Reducer for Question No.1 Task 2:
#
# The reducer aggregates relative humidity measurements by date, ignoring the WBAN Number. 
# It calculates the minimum relative humidity for each date.

# Importing necessary libraries
import sys

# Global variables
current_date = None
min_humidity = float('inf')

# Function to reset min for a new date
def reset_min():
    global min_humidity 
    min_humidity = float('inf')

# Emit the results for the current date
def emit_results(date):
    global min_humidity
    if date and min_humidity != float('inf'):
        print(f"{date}\t{min_humidity}")

        # Reset min for the next date
        reset_min()

# Reducer function to process each line of input
def reducer():
    global current_date, min_humidity

    for line in sys.stdin:

        # Splitting the input to extract date and relative humidity, ignoring WBAN Number
        composite_key, value = line.strip().split('\t')
        _, date = composite_key.split('-', 1)
        relative_humidity = float(value)

        # If the date has changed, emit the results for the previous date
        if date != current_date:

            # Emit results for the previous date
            emit_results(current_date)

            # Set the current date
            current_date = date

        # Update the min relative humidity
        min_humidity = min(min_humidity, relative_humidity)

    # Handle the last date 
    emit_results(current_date)

# Calling the reducer function
if __name__ == "__main__":
    reducer()
