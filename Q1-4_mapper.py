#!/usr/bin/env python3

# Goldsmiths University of London
# MSc. Data Science and Artificial Intelligence
# Module: Big Data Analysis
# Author: Carlos Manuel De Oliveira Alves
# Student: cdeol003
#
# --> Mapper for Question No.1 Task 4:
#
# The mapper needs to parse the Wban Number, YearMonthDay, Relative Humidity, 
# Wind Speed, and Dry Bulb Temp from each record and emit a composite key 
# consisting of the Wban Number and YearMonthDay and a tuple of 
# (Relative Humidity, Wind Speed, Dry Bulb Temp) as the value

import sys

def mapper():

    for line in sys.stdin:

        data = line.strip().split(',')

        if len(data) > 12:

            wban = data[0]
            date = data[1]
            relative_humidity = data[11]  # Relative humidity is in column 12
            wind_speed = data[12]         # Wind speed is in column 13
            dry_bulb_temp = data[8]       # Dry bulb temperature is in column 9

            try:
                relative_humidity = float(relative_humidity)
                wind_speed = float(wind_speed)
                dry_bulb_temp = float(dry_bulb_temp)

                print(f"{wban}-{date}\t({relative_humidity}, {wind_speed}, {dry_bulb_temp})")

            # Skip the line if cannot be converted to float
            except ValueError:
                continue

if __name__ == "__main__":
    mapper()
