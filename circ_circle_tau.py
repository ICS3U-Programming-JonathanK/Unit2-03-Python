#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May 4, 2021
# This program asks the user for the radius of
# a circle in m. It then calculates and displays
# the circumference using tau.
import constants


def main():
    # input
    radius = float(input("Enter the radius of the circle (m): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference = {:.2f} mm".format(circumference))


if __name__ == "__main__":
    main()
