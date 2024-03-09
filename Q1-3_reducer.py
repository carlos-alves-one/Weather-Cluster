#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Reducer for Question No.1 Task 3:
#
# The reducer aggregates dew point temperatures by date, ignoring the WBAN Number. 
# It calculates the mean and variance of dew point temperatures for each date.

# Importing necessary libraries
import sys


# Function to calculate the mean of a list of numbers
def calculate_mean(values):
    return sum(values) / len(values)


# Function to calculate the variance of a list of numbers
def calculate_variance(values, mean):
    squared_deviations = [(x - mean) ** 2 for x in values]
    return sum(squared_deviations) / len(values)


# Global variables
current_date = None
dew_point_temps = []


# Function to emit the results for the current date
def emit_results(date):
    global dew_point_temps

    if date and dew_point_temps:  # Check if date and values exist

        mean_dew_point = calculate_mean(dew_point_temps)
        variance_dew_point = calculate_variance(dew_point_temps, mean_dew_point)

        print(f"{date}\t({mean_dew_point}, {variance_dew_point})")

        # Reset to store data for the next date
        dew_point_temps = [] 


# Reducer function to process each line of input
def reducer():
    global current_date, dew_point_temps

    for line in sys.stdin:
        # Splits the input using a tab to get date and dew point temperature, ignoring WBAN Number
        composite_key, value = line.strip().split('\t')
        _, date = composite_key.split('-', 1)
        dew_point_temp = float(value)

        # If the date has changed, emit the results for the previous date
        if date != current_date:
            emit_results(current_date)
            current_date = date

        # Accumulate the list of dew point temperatures for the current date 
        dew_point_temps.append(dew_point_temp)

    # Handle output for the last date 
    emit_results(current_date)


# Calling the reducer function
if __name__ == "__main__":
    reducer()
