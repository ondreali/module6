"""
program: inner_functions_assignment.py
Author: Ondrea Li
Last date modfied: 06/17/20

The purpose of this program is to write a function measurements that accepts a list of measurements
for a rectangle
and returns a string with perimeter and area
"""
def measurements(a_list):
    """
    reST style
    :param a_list: represents the length
    :return: area of square and rectangle
    """
    #calculates the area
    def area(a_list):
        if len(a_list) >=1:
            square_area = a_list[0] * a_list[0]
            return square_area
        elif len(a_list) <=2:
            rectangle_area = a_list[0] * a_list[1]
            return rectangle_area
    #arguments can be 1 or 2 length list
    #how do i tell if its a square? can i do this based on lenth of the list
        #if its a square, how do i calculate the area?
            #a = side^2; side * side
    #return value
    calculated_area = area(a_list)

    #calculates the perimeter
    def perimeter(a_list):
        """
        reST style
        :param a_list: represents the length
        :return: perimeter of square and rectangle
        """
        if len(a_list) >=1:
            square_perimeter = a_list[0] * 4
            return square_perimeter
        elif len(a_list) <=2:
            rectangle_perimeter = (a_list[0] + a_list[1]) * 2
            return rectangle_perimeter

    calculated_perimeter = perimeter(a_list)
    return f'Perimeter = {calculated_perimeter:.2f} Area = {calculated_area:.2f}'

if __name__ == '__main__':
    square_sides = measurements([1.5])
    print(square_sides)
    rectangle_sides = measurements([6.2, 5.6])
    print(rectangle_sides)

#square_sides perimeter= 6.00 Area = 2.25
#rectangle_sides perimeter= 24.80 Area = 38.44
