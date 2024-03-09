#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Mapper for Question No.1 Task 3:
#
# The mapper needs to parse the Wban Number, YearMonthDay, and Dew Point Temp 
# from each record and emit a composite key consisting of the Wban Number 
# and YearMonthDay and the Dew Point Temp as the value.

# Importing necessary libraries
import sys

# Mapper function to process each line of input
def mapper():

    # Reading input from standard input
    for line in sys.stdin:

        # Splitting the CSV formatted line
        data = line.strip().split(',')

        # Checking if the line has the expected number of columns
        if len(data) > 12:

            # Extracting the Wban Number, YearMonthDay, and Dew Point Temperature
            wban = data[0]
            date = data[1]
            dew_point_temp = data[9]  # dew point temperature is in column 10

            # Emitting the composite key (Wban-Date) and Dew Point Temperature
            try:
                dew_point_temp = float(dew_point_temp)
                print(f"{wban}-{date}\t{dew_point_temp}")

            # Skip the line if dew point temperature is invalid
            except ValueError:
                continue


# Calling the mapper function
if __name__ == "__main__":
    mapper()

