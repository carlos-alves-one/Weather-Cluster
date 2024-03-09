
#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Mapper for Question No.1 Task 1:
#
# The mapper needs to parse the Wban Number, YearMonthDay, and Wind Speed (kt) 
# from each record and emit a composite key consisting of the Wban Number and 
# YearMonthDay and the Wind Speed (kt) as the value.

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

            # Extracting the Wban Number, YearMonthDay, and Wind Speed (kt)
            wban = data[0]
            
            # Extracting the YearMonthDay and removing the dashes
            date = data[1]

            # Extracting the Wind Speed (kt)
            wind_speed = data[12]

            # Emitting the composite key (Wban-Date) and Wind Speed (kt)
            try:

                # Convert wind speed to float to ensure it's a valid number
                wind_speed = float(wind_speed)
                
                # Emit composite key (Wban-Date) and wind speed
                print(f"{wban}-{date}\t{wind_speed}")
            
            # Skip the line if wind speed is not a number
            except ValueError:

                # Skip the line if wind speed is not a number
                continue

# Calling the mapper function
if __name__ == "__main__":
    mapper()
