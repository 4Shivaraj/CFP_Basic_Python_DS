'''
    @Author: Shivaraj
    @Date: 07-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 07-10-2022
    @Title: Write a Python program to calculate the length of a string.
'''

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def calculate_length(self, my_string):
        """
        Description:
            Takes the parameter as my_string and return printing length of string data.
        Parameter:
            Passed parameter my_string as string. 
        Return:
            Returns printing lenth of string data.
        """
        try:
            return lg.info(f"length of string:{len(my_string)}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_string = "shivaraj"
    string_obj = String()
    result = string_obj.calculate_length(my_string)
