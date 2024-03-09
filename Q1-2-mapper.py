
#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Mapper for Question No.1 Task 2:
#
# The mapper needs to parse the Wban Number, YearMonthDay, and Relative Humidity 
# from each record and emit a composite key consisting of the Wban Number 
# and YearMonthDay and the Relative Humidity as the value.

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
        
            # Extracting the Wban Number, YearMonthDay, and Relative Humidity
            wban = data[0]
            date = data[1]
            relative_humidity = data[11]  

            # Emitting the composite key (Wban-Date) and Relative Humidity
            try:

                # Convert relative humidity string to float for validation
                relative_humidity = float(relative_humidity)

                # Emit Wban, date and relative humidity
                print(f"{wban}-{date}\t{relative_humidity}")

            # Skip the line if relative humidity is not a valid number
            except ValueError:
                continue

# Calling the mapper function
if __name__ == "__main__":
    mapper()

