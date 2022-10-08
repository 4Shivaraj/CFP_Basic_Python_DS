from data_log import get_logger


'''
    @Author: Shivaraj
    @Date: 07-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 07-10-2022
    @Title: Write a Python program to count occurrences of a substring in a string.
'''


lg = get_logger(name="(program_10)", file_name="data_log.log")


class String:
    """
    string Manipulations
    """

    def count_sub_string(self, sample_text: str):
        """
        Description:
            Takes the parameter as my_string and return count occurrences of a substring in a string.
        Parameter:
            Passed parameter sample_text as string.
        Return:
            Returns count occurrences of a substring in a string.
        """
        try:
            return lg.info(
                f"text :{sample_text} and count of sub-string 'for': {sample_text.count('for')} ")

        except Exception as e:
            lg.exception(e)


if __name__ == "__main__":
    sample_text = 'This channel is focused on creating tutorials for frontend and for backend developers'
    string_obj = String()
    result = string_obj.count_sub_string(sample_text)
