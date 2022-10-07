'''
    @Author: Shivaraj
    @Date: 06-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 06-10-2022
    @Title: Write a Python program to count the number of strings where the string length
            is 2 or more and the first and last character are same from a given list of strings.
            Sample List : ['abc', 'xyz', 'aba', '1221']
            Expected Result : 2
'''

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class List:
    """
    List Manipulations
    """

    def count_string(self, my_list: list):
        """
        Description:
            Takes the parameter as list and return print of number of string matched with first and last letter.
        Parameter:
            Passed parameter my_list as list. 
        Return:
            Returns print of number of string matched with first and last letter.
        """
        try:
            lg.info(f"original list: {my_list}")
            count = 0
            for element in my_list:
                if len(element) > 1 and element[0] == element[-1]:
                    count += 1
            return lg.info(f"The {count} number of strings are matched, where string length is greater than 1 and first and last charater are same.")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    my_list = ['1221', 'shiv', 'raj', 'lola', 'pradeep']
    list_obj = List()
    list_obj.count_string(my_list)
