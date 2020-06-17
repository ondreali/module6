"""
program: valid_input_in_functions.py
Author: Ondrea Li
Last date modfied: 06/16/20

The purpose of this program is to write a function
ask the user for a valid test score until it is in the range,
the print valid input as 'Test name:##'.
"""
def score_input(test_name, test_score = 0, invalid_message= 'Please try again'):
    """
    Use reST style
    :param test_name: this represents the user's test name
    :param test_score: this represents test score
    :param invalid_message: this represents message if input invalid
    : return: test_name: test_score
    : raises keyError: raises an exception
    """
    while True:
        try:
            test_score = int(input("Please enter test score: "))
            if 0 <= test_score and test_score <= 100:
                return f'{test_name}:{test_score}'
            else:
                return f'{test_name}:{test_score}, {invalid_message}'
        except ValueError:
            print("Value Error, err!")
            raise ValueError



if __name__ == '__main__':
    try:
        test_name = input("Please enter your name:")
        test_score = int(input("Please enter test score: "))
        invalid_message = "Invalid test score, try again"
    except ValueError as err:
        print("ValueError encountered")
    else:
        print(score_input(test_name, test_score, invalid_message))


