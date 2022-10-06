'''
    @Author: Shivaraj
    @Date: 03-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 03-10-2022
    @Title: Write a Python program to list all files in a directory in Python.
'''

import subprocess
from data_log import get_logger

lg = get_logger(name="(program_14)", file_name="data_log.log")


if __name__ == "__main__":
    subprocess.call(['ls', '*py'])
