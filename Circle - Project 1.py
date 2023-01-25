# Project #1 - Part 3 of 3 (Circle)
# Student: Rene Tejon
# Student ID: rt891
# Course CRN and Section: 31344 - L01
# Course: MSIT 501 - Foundations of Programming, Data Structures, and Algorithms
# Professor: Dr. Frank J Mitropoulos Ph.D.
# Due Date: January 16, 2022

"""This is a Python script that creates an estimate for the customer,
 based on the cost of materials and installation for the area of a circular room."""


from math import pi


def main():

    print('Estimate for a Circular Room\n')

    name_of_customer = input('What is the name of the customer? ')
    address_of_customer = input('What is the address of the customer? ')
    diameter_of_room = eval(input('What is the diameter of the room (in feet)? '))
    radius_of_room = diameter_of_room / 2
    area_of_circle_room = (radius_of_room ** 2) * pi
    material_cost = area_of_circle_room * 2
    installation_cost = area_of_circle_room * 1.50

    print(f'\nEstimate for {name_of_customer}\n{address_of_customer}\n')
    print(f'Circular room with area of {round(area_of_circle_room, 2)} square feet')
    print(f'Estimated cost for flooring material is ${material_cost:.2f}')
    print(f'Estimated cost for installation is ${installation_cost:.2f}')
    print(f'Total estimate is ${material_cost + installation_cost:.2f}')


if __name__ == '__main__':

    main()

print(input('\nPress Enter to exit'))
