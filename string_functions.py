"""
program: Function_return_value.pry
Author: Ondrea Li
Last date modfied: 06/16/20

The purpose of this program is to write a string and print message
"""

def multiple_string(n, message):
    """
    Use reST style
    :param
    :param
    : return: weekly pay
    : raises keyError: raises an exception
    """
    # takes a strung message and a number n
    while True:
        try:
            for line in range(n):
                if n < 1 and n > 9:
                    print("n must be between 1 and 9")
                else:
                    break
        except ValueError:
            print("Value error!")
            pass
        if 1<= n <= 9:
            print("valid")
        else:
            print("invalid")
            break
        return str(n * message) # returns the strung with message printed n times
if __name__ == '__main__':
    try:
        message = input("enter word: ")
        n = int(input("Enter number of times to print"))
    except ValueError:
        print("ValueError found!!")
    else:
        print(multiple_string(n, message))
