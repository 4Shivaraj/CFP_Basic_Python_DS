'''
    @Author: Shivaraj
    @Date: 07-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 07-10-2022
    @Title: Write a Python program to display formatted text (width=50) as output.
'''
import textwrap

from numpy import safe_eval
from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def format_text(self, sample_text):
        """
        Description:
            Takes the parameter as my_string and return displaying formatted text (width=50) as output.
        Parameter:
            Passed parameter sample_text as string.
        Return:
            Returns displaying formatted text (width=50) as output.
        """
        try:
            return lg.info(
                f"displaying formated text :{textwrap.fill(sample_text, width=50)}")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    sample_text = '''Python is a widely used high-level, general-purpose, interpreted,
                    dynamic programming language. Its design philosophy emphasizes
                    code readability, and its syntax allows programmers to express
                    concepts in fewer lines of code than possible in languages such
                    as C++ or Java.   '''

    string_obj = String()
    result = string_obj.format_text(sample_text)
