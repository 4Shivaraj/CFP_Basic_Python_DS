'''
    @Author: Shivaraj
    @Date: 07-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 07-10-2022
    @Title: Write a Python program to create a tuple with different data types.
'''

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class Tuples:
    """
    Tuple Manipulations
    """

    def create_tuples(self, my_tuple):
        """
        Description:
            Takes the parameter as my_tuple and return printing the tuple data with different data types.
        Parameter:
            Passed parameter my_tuple as tuple. 
        Return:
            Returns printing the tuple data with different data types.
        """
        try:
            return lg.info(f"type of data:{type(my_tuple)} and data: {my_tuple}")
        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_tuple = (1, 2.0, 'shiv', True, 2+5j)
    tuple_obj = Tuples()
    result = tuple_obj.create_tuples(my_tuple)
