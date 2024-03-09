#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Reducer for Question No.1 Task 4:
#
# The reducer calculates the correlation matrix among the Relative Humidity, Wind Speed, and 
# Dry Bulb Temp for each date and ignores the WBAN Number.

import sys
import numpy as np

# Function to calculate the Pearson Correlation Coefficient
def calculate_pearson_correlation(x, y):
    n = len(x)  # Assume equal length for x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    std_x = np.std(x)
    std_y = np.std(y)

    # Pearson Correlation formula
    covariance = np.sum((x - mean_x) * (y - mean_y))
    correlation = covariance / (n * std_x * std_y)

    return correlation

# Global variables
current_date = None
measurements = []

# Function to emit the results for the current date
def emit_results(date):
    global measurements 

    if date and measurements:  # Check if date and values exist

        # Unpack data for calculation (using numpy for efficiency)
        relative_humidity, wind_speed, dry_bulb_temp = np.array(measurements).T

        # Calculate pairwise correlations
        corr_humidity_wind = calculate_pearson_correlation(relative_humidity, wind_speed)
        corr_humidity_temp = calculate_pearson_correlation(relative_humidity, dry_bulb_temp)
        corr_wind_temp = calculate_pearson_correlation(wind_speed, dry_bulb_temp)

        print(f"{date}\t({corr_humidity_wind}, {corr_humidity_temp}, {corr_wind_temp})")

        # Reset to store data for the next date
        measurements = []

# Reducer function to process each line of input
def reducer():
    global current_date, measurements

    for line in sys.stdin:
        # Splits the input using a tab to get date and measurements, ignoring WBAN Number
        composite_key, values = line.strip().split('\t')
        _, date = composite_key.split('-', 1)

        # Parse tuple as an array for ease of handling
        relative_humidity, wind_speed, dry_bulb_temp = eval(values)

        # If the date has changed, emit the results for the previous date
        if date != current_date:
            emit_results(current_date)
            current_date = date

        # Accumulate the list of measurements for the current date 
        measurements.append([relative_humidity, wind_speed, dry_bulb_temp])

    # Handle output for the last date 
    emit_results(current_date)

if __name__ == "__main__":
    reducer()

