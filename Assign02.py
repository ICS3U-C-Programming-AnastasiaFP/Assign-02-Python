#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: October. 14, 2023
# Program that calculates the area and perimeter of a pentagon

import math


def main():
    # get length
    length = int(input("Enter Length of a Side: "))
    print("")

    # get units
    units = input("Enter Units: ")
    print("")

    # calculate perimeter
    perimeter = 5 * length
    # calculate area
    area = 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5)) * length**2)
    # display P and A with units
    print(perimeter, units)
    print(area, units, 2)


if __name__ == "__main__":
    main()
