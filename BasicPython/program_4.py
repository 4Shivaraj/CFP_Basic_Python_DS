'''
    @Author: Shivaraj
    @Date: 03-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 03-10-2022
    @Title: Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
'''

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


if __name__ == "__main__":
    lg.info(abs.__doc__)
