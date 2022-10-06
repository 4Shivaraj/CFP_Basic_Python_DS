'''
    @Author: Shivaraj
    @Date: 04-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 04-10-2022
    @Title: Write a python program to call an external command in Python.
'''

import subprocess
from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


if __name__ == "__main__":
    subprocess.call(["ls", "-al"])
