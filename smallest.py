#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on June 2021
# This program finds the smallest of 10 random numbers

import random


def find_smallest(numbers):
    # This function determines the smallest number

    # Set default value for smallest
    smallest = numbers[0]

    # Loop through "array" to find smallest
    for counter in numbers:
        if counter < smallest:
            smallest = counter

    return smallest


def main():
    # This function generates 10 numbers

    random_numbers = []

    # Process and output
    for loop_counter in range(0, 10):
        generated_number = random.randint(1, 100)
        random_numbers.append(generated_number)
        print("Random number {0} is {1}.".format(
            loop_counter + 1, random_numbers[loop_counter]
        ))
    # Call find_smallest
    smallest_number = find_smallest(random_numbers)
    print("\nThe smallest number is {}.".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
