'''
    @Author: Shivaraj
    @Date: 03-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 03-10-2022
    @Title: Write a python program to access environment variables.
'''

import os
from data_log import get_logger

lg = get_logger(name="(program_15)", file_name="data_log.log")


if __name__ == "__main__":
    lg.info(os.environ.get('EMAIL_HOST_USER'))
