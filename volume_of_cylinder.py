#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program calculates the volume of a cylinder

import math


def main():
    # this function calculates the volume of a cylinder

    # input
    radius_of_cylinder = float(input("Enter radius of the cylinder (mm): "))
    height_of_cylinder = float(input("Enter height of the cylinder (mm): "))
    # process
    volume_of_cylinder = math.pi * radius_of_cylinder**2 * height_of_cylinder

    # output
    print("")
    print("Volume is {0:,.2f} mm.".format(volume_of_cylinder))

    print("\nDone.")


if __name__ == "__main__":
    main()
