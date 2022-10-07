'''
    @Author: Shivaraj
    @Date: 06-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 06-10-2022
    @Title: Write a Python program to clear a set.
'''

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


if __name__ == "__main__":
    my_set = set([7, 5, 3, 4, 5, 6, 1])
    lg.info(f"set details: {my_set}")
    choice = input("Do you want to clear a set? Enter y for yes: ")
    if choice == 'y':
        my_set.clear()
        lg.info(f'cleared all the elements: {my_set}')
    else:
        lg.info(my_set)
